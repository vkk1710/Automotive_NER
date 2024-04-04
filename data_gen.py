import os
import openai
import json
import pandas as pd
from templates import TEMPLATES
from jsonschema import Validator, validate


def define_validation_schema():
    schema = None
    try:
        schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Sentence": {"type": "string"},
                    "Output": {
                        "type": "array",
                        "items": {"type": "object",
                                  "properties": {
                                      "Entity": {"type": "string"},
                                      "Label": {"type": "string"}
                                  }
                                  },
                    }
                },
                "required": ["Sentence", "Output"],
            }
        }
        Validator.check_schema(schema)
    except Exception as error:
        print("Not a valid schema, Error:", error)

    return schema


class DataGeneration:
    def __init__(self, count=5, batch=5, templates_batch=3):
        self.count = count
        self.batch = batch
        self.templates_batch = templates_batch

        self.templates = TEMPLATES
        self.validation_schema = define_validation_schema()

        # Insert your OpenAI API key before proceeding further
        os.environ["OPENAI_API_KEY"] = ""
        self.client = openai.OpenAI()

    def ask_gpt(self, prompt):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    def generate_data(self):
        num_temps = len(self.templates)
        steps = self.count // self.batch

        new_data = []
        print('Data Generation Started!')
        for i in range(num_temps - self.templates_batch):
            print(f'Generating data for templates {i+1}-{(i + self.templates_batch) % num_temps}...')
            prompt_inps = self.templates[i:(i + self.templates_batch) % num_temps]
            prompt = f"""
            Here is a list of different data instances for the NER task in the automotive domain - 
            {str(prompt_inps)}
    
            Generate a list of {self.batch} such sentence, output pairs with the whole result in JSON format having an 
            array in the above format only. Remember to annotate the following entities only - Component, Failure_issue, Vehicle_model, Corrective_action, Manufacturer, Recall_date. Also try to generate meaningful sentences of minimum 60 tokens.
          """

            for _ in range(steps):
                valid_data = False
                while not valid_data:
                    try:
                        out = self.ask_gpt(prompt)
                        json_object = json.loads(out)
                        validate(instance=json_object, schema=self.validation_schema)

                        new_data += list(json_object)
                        valid_data = True

                    except Exception as err:
                        print(f"Encountered an error. \nSo, re-generating data!")
        return new_data


if __name__ == "__main__":
    data_gen_obj = DataGeneration(count=150, batch=5, templates_batch=3)
    generated_data = data_gen_obj.generate_data()
    gen_data_df = pd.DataFrame(generated_data)
    gen_data_df.to_csv('./data/gpt_gen_data.csv')

