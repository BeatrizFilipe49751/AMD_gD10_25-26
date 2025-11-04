import csv, json
from collections import defaultdict, Counter

# Load the trained model
with open("one_rule_model.json", "r", encoding="utf-8") as f:
    model = json.load(f)

attr = model["attribute"]
rule = model["rule"]

# File paths
input_path  = r"C:\Users\Ana Sofia\Documents\ISEL\SEMESTRE 1\AMD\projectA\new_patients.csv"
output_path = r"C:\Users\Ana Sofia\Documents\ISEL\SEMESTRE 1\AMD\projectA\predictions.csv"

# Read new patient data
with open(input_path, newline='', encoding='utf-8') as f_in, \
     open(output_path, "w", newline='', encoding='utf-8') as f_out:

    reader = csv.DictReader(f_in)
    fieldnames = reader.fieldnames + ["predicted_lenses"]
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        row["predicted_lenses"] = rule.get(row[attr], "unknown")
        writer.writerow(row)

print(f"Predictions saved to {output_path}")