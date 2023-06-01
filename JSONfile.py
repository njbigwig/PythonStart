import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

# convert CSV to JSON format
einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print("JSON: ", einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as csvinputfile:
    reader = csv.DictReader(csvinputfile)
    laureates = list(reader)


with open("laureates.json", "w") as jsonoutputfile:
    json.dump(laureates, jsonoutputfile, indent=2)