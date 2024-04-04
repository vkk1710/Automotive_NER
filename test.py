from utils import *
import argparse
import warnings
warnings.filterwarnings('ignore')


def test(paragraph, args):
    try:
        model, tokenizer = load_phi2(args, testing=True)
        output = predict_phi2(paragraph=input_txt, model=model, tokenizer=tokenizer, args=args).split('Answer:')[
            1].strip()
        return output

    except Exception as err:
        print(f"An Error Occurred - {err}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, help='A required string argument')

    user_args = parser.parse_args()
    input_txt = user_args.text

    if input_txt is None:
        print("Invalid Input! Enter Again.")

    config_path = "configs/config.json"
    args = load_config(config_path)

    output = test(input_txt, args)

    print("\nText:")
    print(input_txt)
    print("\n")
    print("Entities:")
    print(output)
