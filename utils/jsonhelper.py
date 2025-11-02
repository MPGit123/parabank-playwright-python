import json
import os

def load_json_data(file_name: str):
    file_path = os.path.join("testdata", file_name)
    with open(file_path) as file:
        return json.load(file)