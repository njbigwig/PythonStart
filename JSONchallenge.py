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

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as csvinput:
    reader = csv.DictReader(csvinput)
    laureates = list(reader)


# 1. you can access parts of strings the same way you do lists
#      hey[2] == "y"
# 2. You can add to a list using
#      my_list.append("something")

laureates_beginning_with_a = []
# LinkedIn learner code here - find all laureates whose first name starts with A
# LinkedIn solution - more efficient:
#    if lareate['name'][0] == "A":

for laureate in laureates:
    firstname = laureate["name"]
    if firstname[0] == "A":
        laureates_beginning_with_a.append(laureate)
        pprint(laureate)

print("Laureates first name starts with A: ", len(laureates_beginning_with_a))

with open("laureates.json", "w") as jsonoutput:
    json.dump(laureates_beginning_with_a, jsonoutput, indent=2)