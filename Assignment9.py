import csv
import json

with open("data.csv", "r") as csv_file:
    data = list(csv.DictReader(csv_file))

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data converted to JSON successfully.")
