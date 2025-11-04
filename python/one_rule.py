import csv
from collections import defaultdict, Counter
import json

# Function to load dataset from CSV file
def load_dataset(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

# Train the 1R model
def train_one_rule(rows, target):
    features = [f for f in rows[0] if f != target]
    best_attr, best_rule, best_acc = None, None, 0

    for attr in features:
        groups = defaultdict(list)
        for r in rows:
            groups[r[attr]].append(r[target])

        # Rule: for each attribute value, choose the most common class
        rule = {v: Counter(vals).most_common(1)[0][0] for v, vals in groups.items()}

        # Calculate accuracy
        correct = sum(1 for r in rows if rule.get(r[attr]) == r[target])
        acc = correct / len(rows)

        if acc > best_acc:
            best_attr, best_rule, best_acc = attr, rule, acc

    return {"attribute": best_attr, "rule": best_rule, "accuracy": best_acc}

# Main program
if __name__ == "__main__":
    # Path to your dataset
    dataset = load_dataset(r"C:\Users\Ana Sofia\Documents\ISEL\SEMESTRE 1\AMD\projectA\lenses.csv")

    # Train the model
    model = train_one_rule(dataset, "lenses")

    print("=== 1R Model Trained ===")
    print(f"Best Attribute: {model['attribute']}")
    print("Rule:")
    for k, v in model["rule"].items():
        print(f"  if {model['attribute']} = {k} → lenses = {v}")
    print(f"\nAccuracy: {model['accuracy']*100:.2f}%")

    # Save model
    with open("one_rule_model.json", "w", encoding="utf-8") as f:
        json.dump(model, f, indent=4)
    print("\nModel saved → one_rule_model.json")
