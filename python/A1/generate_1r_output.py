from collections import defaultdict
import sys
from typing import Any, Dict, List
from sklearn.calibration import LabelEncoder
import pandas as pd
from ..models.one_rule import OneRuleClassifier
# Import preprocessing and configuration paths
from ..utils.preprocessing import preprocess_data
from ..utils import config

def generate_1r_output(model: Dict[str, Any],
                       train_rows: List[Dict[str, Any]],
                       target: str,
                       feature_encoders: dict,
                       target_encoder: LabelEncoder):
    attr = model["feature"]
    rule = model["rule"]

    # Count totals and errors
    stats = defaultdict(lambda: defaultdict(lambda: {"total": 0, "error": 0}))

    for row in train_rows:
        value_attr_encoded = row[attr]
        value_target_encoded = row[target]

        predicted_encoded = rule[value_attr_encoded]

        stats[value_attr_encoded][value_target_encoded]["total"] += 1
        if predicted_encoded != value_target_encoded:
            stats[value_attr_encoded][value_target_encoded]["error"] += 1

    # Write output file with decoded names
    attr_le = feature_encoders[attr]
    with open(config.ONER_OUTPUT_PATH, "w") as f:
        for value_attr_encoded, target_map in stats.items():
            value_attr = attr_le.inverse_transform([value_attr_encoded])[0]  # decode feature value
            for value_target_encoded, info in target_map.items():
                value_target = target_encoder.inverse_transform([value_target_encoded])[0]  # decode class
                f.write(f"({attr}, {value_attr}, {value_target}) : ({info['error']}, {info['total']})\n")

    print(f"1R output written successfully.")
    
    
def main(target_column: str):
    # Load dataset
    df = pd.read_csv(config.DATASETA1_PATH)

    # Encode all features and target
    X, y, feature_encoders, target_encoder = preprocess_data(df, target_column, False)

    # Train 1R
    oner_model = OneRuleClassifier().fit(X, y)

    # Prepare rows for output
    df_encoded = X.copy()
    df_encoded[target_column] = y
    train_rows = df_encoded.to_dict(orient="records")

    # Generate output file
    generate_1r_output(oner_model.model_, train_rows, target_column, feature_encoders, target_encoder)
    
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_1r_output.py <target_column>")
        sys.exit(1)

    target_column = sys.argv[1]

    main(target_column)