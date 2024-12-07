import openai
import os
import csv
import json
import unicodedata
import time
import random
api_key=os.environ['API_KEY']
openai.api_key = api_key
# Initialize an array to store prompts and responses
csv_json = []

def clean_text(text):
    if not text:
        return ""
    normalized = unicodedata.normalize('NFKD', text)
    ascii_text = normalized.encode('ascii', 'ignore').decode('ascii')
    cleaned_text = ' '.join(ascii_text.split())
    return cleaned_text

def get_completion(csv_file_path):
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]  # Get all rows from the CSV
            random_rows = random.sample(rows, 12)  # Select 12 random rows
            for row in random_rows:
                temp_obj = {}
                for key, value in row.items():
                    temp_obj[key] = value
                try:
                    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=f"""describe a special power (programming and coding related) of {clean_text(temp_obj["player_name"])}. This person has a codewars score of {temp_obj["score"]}""", max_tokens=60, temperature=0.75)
                    temp_obj["special_power"] = response.choices[0].text.strip()
                    response_t = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=f"""describe the future potential (programming and coding related) of {clean_text(temp_obj["player_name"])}, with a codewars score of {temp_obj["score"]}. only provide the future potential description.""", max_tokens=60, temperature=0.75)
                    temp_obj["future_potential"] = response_t.choices[0].text.strip()
                    response_fji = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=f"""{clean_text(temp_obj["player_name"])} has a  codewars score of {temp_obj["score"]}, and can be described with {temp_obj["special_power"]}, {temp_obj["future_potential"]}.  provide one emoji that fits well with the person. only return the emoji.""", max_tokens=5, temperature=0.50)
                    temp_obj["emoji"] = response_fji.choices[0].text.strip()
                except Exception as e:
                    print(f"Error generating player summary: {e}")
                finally:
                    time.sleep(.25)
                    if "player_name" in temp_obj:
                        csv_json.append(temp_obj)
        if csv_json:
            with open('quotes.json', 'w') as file:
                json.dump(csv_json, file, indent=4)
    except Exception as e:
        print(f"Error processing completion: {e}")