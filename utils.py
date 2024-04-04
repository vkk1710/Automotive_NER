import replicate
import torch
import json
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


def load_config(config_path):
    try:
        with open(config_path) as file:
            args = json.load(file)

    except Exception as err:
        print(f"Error while opening the config.json file - {err}")

    return args


def predict_llama(paragraph):
    inp = {
        "debug": False,
        "top_p": 1,
        "prompt": f"Text: {paragraph} Task: Extract the following entities out of the given text in the form of a JSON object without any explanations - [component, failure issue, vehicle model, corrective action].",
        "temperature": 0.75,
        "system_prompt": "You are a helpful, respectful and honest assistant. You will be given a Text and you have to complete the Task with the help of the given Text only. Give the output in the form of a JSON object.",
        "max_new_tokens": 500,
        "min_new_tokens": -1,
        "prompt_template": "[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST]",
        "repetition_penalty": 1
    }

    output = replicate.run(
        "meta/llama-2-70b-chat",
        input=inp
    )
    return ''.join(output)


def load_phi2(args=None, testing=False):
    base_model_name = "microsoft/phi-2"

    if args is None:
        model = AutoModelForCausalLM.from_pretrained(base_model_name, torch_dtype="auto", device_map="auto",
                                                     trust_remote_code=True)
        tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)

    else:
        base_model_name = args["base_model"]
        device_map = args["device_map"]

        bnb_config = BitsAndBytesConfig(load_in_4bit=args["bnb_config"]["load_in_4bit"],
                                        bnb_4bit_quant_type=args["bnb_config"]["bnb_4bit_quant_type"],
                                        bnb_4bit_compute_dtype=args["bnb_config"]["bnb_4bit_compute_dtype"],
                                        bnb_4bit_use_double_quant=args["bnb_config"]["bnb_4bit_use_double_quant"])

        model = AutoModelForCausalLM.from_pretrained(base_model_name,
                                                          device_map=device_map,
                                                          quantization_config=bnb_config,
                                                          attn_implementation=args["base_model_attn_implementation"],
                                                          trust_remote_code=True)

        tokenizer = AutoTokenizer.from_pretrained(base_model_name,
                                                  add_eos_token=True,
                                                  trust_remote_code=True)
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.truncation_side = args["tokenizer_config"]["truncation_side"]

        if testing:
            # Load the model weights from hub
            model_id = args["hf_username"] + "/" + args["new_model_name"]
            model = PeftModel.from_pretrained(model, model_id)

    return model, tokenizer


def predict_phi2(paragraph, model, tokenizer, args=None):
    if args is None:
        tokenizer_padding = False
        tokenizer_truncation = False
        skip_special_tokens = False
        torch.set_default_device("cuda")
        max_length = 500
        prompt = f"""Text: {paragraph} Now extract the following entities from the given text -  component, failure issue, vehicle model, corrective action. Give the output in the form of JSON."""

    else:
        tokenizer_padding = True
        tokenizer_truncation = True
        skip_special_tokens = True
        device_map = args["device_map"]
        max_length = 1000
        prompt = f"""###System:
            You are a helpful, respectful and honest assistant. You will be given a Text and you have to extract the following entities from this text - [Component, Failure_issue, Vehicle_model, Corrective_action, Manufacturer, Recall_date]. Do not generate something that is not present in the Text given. Give the output in the form of a JSON.
            ###Text:
            {paragraph}
            ###Answer:
            """

    inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=False, padding=tokenizer_padding, truncation=tokenizer_truncation)

    if args is not None and args["device_map"] in ["auto", "cuda"]:
        inputs.to('cuda')

    outputs = model.generate(**inputs, max_length=max_length)
    text = tokenizer.batch_decode(outputs, skip_special_tokens=skip_special_tokens)[0]

    return text
