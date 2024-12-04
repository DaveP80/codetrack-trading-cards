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

def get_completion(prompt, csv_file_path):
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
                    response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt=f"""{prompt}: {clean_text(temp_obj["player_name"])} {temp_obj["score"]}""", max_tokens=115, temperature=0.75)
                    temp_obj["player_summary"] = response.choices[0].text.strip()
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
