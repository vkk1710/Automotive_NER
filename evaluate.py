import os
import pandas as pd

from utils import *


def evaluate(test_file, config_path, results_file_path):
    df = pd.read_csv(test_file)
    sentences = list(df['Sentence'])

    llama_preds = list()
    phi2_preds = list()
    phi2_finetuned_preds = list()

    args = load_config(config_path)

    base_model, base_tokenizer = load_phi2()
    model, tokenizer = load_phi2(args, testing=True)

    for s in sentences:
        llama_preds.append(predict_llama(s))
        phi2_preds.append(predict_phi2(paragraph=s, model=base_model, tokenizer=base_tokenizer))
        phi2_finetuned_preds.append(predict_phi2(paragraph=s,
                                                 model=model,
                                                 tokenizer=tokenizer,
                                                 args=args).split('Answer:')[1].strip())

    df['LlaMa Predictions'] = llama_preds
    df['Phi2 Predictions'] = llama_preds
    df['Fine-tuned Phi2 Predictions'] = llama_preds

    df.to_csv(results_file_path)


if __name__ == "__main__":
    try:
        # Insert your Replicate Token here before running this file. You can generate a token here - https://replicate.com/account/api-tokens
        os.environ["REPLICATE_API_TOKEN"] = ""

        test_file = "data/test.csv"
        config_path = "configs/config.json"
        results_file_path = "./results.csv"

        evaluate(test_file, config_path, results_file_path)
    except Exception as err:
        print(f"Some Error has Occurred : {err}")







