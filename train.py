import pandas as pd
import datasets
import json
from huggingface_hub import login
from accelerate import FullyShardedDataParallelPlugin, Accelerator
from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model
from torch.distributed.fsdp.fully_sharded_data_parallel import FullOptimStateDictConfig, FullStateDictConfig
from transformers import TrainingArguments, Trainer, HfArgumentParser, BitsAndBytesConfig, AutoModelForCausalLM, \
    AutoTokenizer

from utils import load_config, load_phi2


class ModelTrainer:
    def __init__(self, args):
        self.load_in_4bit = args['bnb_config']['load_in_4bit']
        self.bnb_4bit_quant_type = args['bnb_config']['bnb_4bit_quant_type']
        self.bnb_4bit_compute_dtype = args['bnb_config']['bnb_4bit_compute_dtype']
        self.bnb_4bit_use_double_quant = args['bnb_config']['bnb_4bit_use_double_quant']

        self.base_model_name = args['base_model']
        self.base_model_attn_imp = args['base_model_attn_implementation']
        self.tokenizer_truncation_side = args['tokenizer_config']['truncation_side']
        self.max_length = args['tokenizer_config']['max_length']

        self.device_map = args['device_map']
        self.train_data_path = args['train_data_path']
        self.test_data_split = args['train_test_split']

        self.lora_r = args['lora_config']['r']
        self.lora_alpha = args['lora_config']['lora_alpha']
        self.lora_target_modules = args['lora_config']['target_modules']
        self.lora_bias = args['lora_config']['bias']
        self.lora_dropout = args['lora_config']['lora_dropout']
        self.lora_task_type = args['lora_config']['task_type']

        self.training_args_json = args['training_args_json']
        self.new_model_name = args['new_model_name']
        self.push_to_hub = args['push_to_hub']

        self.df = None
        self.dataset = None
        self.train_dataset = None
        self.test_dataset = None

        self.base_model, self.tokenizer = load_phi2(args, testing=False)
        self.model = None

        self.data_prep()

    def data_prep(self):
        self.df = pd.read_csv(self.train_data_path)
        self.dataset = self.data_preprocess()
        self.train_dataset, self.test_dataset = self.tokenize_data()

    def data_preprocess(self):
        text = self.df['Sentence']
        response = self.df['Output']

        data = list()
        system_prompt = "You are a helpful, respectful and honest assistant. You will be given a Text and you have to extract the following entities from this text - [Component, Failure_issue, Vehicle_model, Corrective_action, Manufacturer, Recall_date]. Do not generate any entity that is not present in the Text given. Give the output in the form of a JSON."

        for txt, resp in zip(text, response):
            prompt_template = f"""###System:
              {system_prompt}
              ###Text:
              {txt}
              ###Answer:
              {resp}"""

            data.append(prompt_template)

        df = pd.DataFrame({'text': data})
        dataset = datasets.Dataset.from_pandas(df)

        return dataset

    def tokenize(self, examples):
        text = examples["text"][0].replace('"', r'\"')
        text = text.replace('"', r'\"')

        encoded = self.tokenizer(
            text,
            return_tensors="np",
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
        )

        encoded["labels"] = encoded["input_ids"]
        return encoded

    def tokenize_data(self):
        shuffled_dataset = self.dataset.shuffle(seed=42)
        split_data = shuffled_dataset.train_test_split(test_size=self.test_data_split)

        # tokenize the training and test datasets
        train_dataset = split_data["train"].map(self.tokenize,
                                                batched=True,
                                                batch_size=1,
                                                remove_columns=["text"])
        test_dataset = split_data["test"].map(self.tokenize,
                                              batched=True,
                                              batch_size=1,
                                              remove_columns=["text"])

        return train_dataset, test_dataset

    def load_training_args(self):
        parser = HfArgumentParser(TrainingArguments)
        training_args, = parser.parse_json_file(json_file=self.training_args_json)

        return training_args

    def train(self):
        fsdp_plugin = FullyShardedDataParallelPlugin(
            state_dict_config=FullStateDictConfig(offload_to_cpu=True, rank0_only=False),
            optim_state_dict_config=FullOptimStateDictConfig(offload_to_cpu=True, rank0_only=False),
        )

        accelerator = Accelerator(fsdp_plugin=fsdp_plugin)

        self.base_model.gradient_checkpointing_enable()
        self.base_model = prepare_model_for_kbit_training(self.base_model, use_gradient_checkpointing=True)

        config = LoraConfig(
            r=self.lora_r,
            lora_alpha=self.lora_alpha,
            target_modules=self.lora_target_modules,
            bias=self.lora_bias,
            lora_dropout=self.lora_dropout,
            task_type=self.lora_task_type
        )

        self.model = get_peft_model(self.base_model, config)
        self.model = accelerator.prepare_model(self.model)

        training_args = self.load_training_args()

        trainer = Trainer(
            model=self.model,
            train_dataset=self.train_dataset,
            eval_dataset=self.test_dataset,
            args=training_args,
        )

        trainer.train()
        print(f"Training completed!")

        if self.push_to_hub:
            self.model.push_to_hub(self.new_model_name, use_auth_token=True, commit_message="Fine-tuning Phi-2 "
                                                                                            "Version-3")


if __name__ == '__main__':
    config = "./configs/config.json"
    args = load_config(config)

    # Place your huggingface access token in the config.json file before training!
    access_token = args["hf_access_token"]
    login(token=access_token)

    m = ModelTrainer(args)
    m.train()
