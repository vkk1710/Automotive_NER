# Automotive_NER
This is my code for the Predii Automotive NER assignment. 

## Installing the required libraries

```
pip install -r requirements.txt
```

If you face any issues installing the libraries with requirements.txt, use the following commands -

```
pip install einops datasets bitsandbytes accelerate peft flash_attn
pip uninstall -y transformers
pip install git+https://github.com/huggingface/transformers
pip install --upgrade torch
pip install replicate
pip install openai
pip install jsonschema
```

## Generating Artificial Data
Generate labeled data artificially using OpenAI gpt-3.5-turbo LLM. Before generating the data, set the OpenAI_API_Key as an environment variable. You can generate the OpenAI_API_Key from <https://platform.openai.com/api-keys>.

```
os.environ["OPENAI_API_KEY"] = <YOUR_OPENAI_API_KEY>
```

To generate the data, run datag_gen.py -

```
python data_gen.py
```

This will save the data in data/gpt_gen_data.csv. You can change the name of the csv file in data_gen.py.

## Fine-tuning
Fine-tune the Microsoft Phi-2 model by running train.py. Before running this train.py, set the training configs in configs/config.json.

```
python train.py
```

Generate a HuggingFace access token and set it in configs/config.json - 

```
"hf_access_token": <YOUR_HF_ACCESS_TOKEN>
```

## Evaluation
We evaluate the LlaMa 2 7b, Phi-2 and the fine-tuned Phi-2 models on data/test.csv. For evaluation, run evaluate.py after setting the Replicate API token as an environment variable. You can generate the Replicate_API_Token from <https://replicate.com/account/api-tokens>

```
os.environ["REPLICATE_API_TOKEN"] = <YOUR_REPLICATE_API_TOKEN>
```

## Testing The Model On Your Text
Test the model on your text by running the test.py file -

```
python test.py --text <YOUR_TEXT>
```






