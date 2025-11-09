import pandas as pd
import sys
from ..utils.load_models import load_1R, load_encoders
from ..utils.transform_new_data import transform_new_data

def predict_1R(input_csv_path: str) -> pd.DataFrame:
    oner_model = load_1R()
    feature_encoders, target_encoder = load_encoders()

    df_new = pd.read_csv(input_csv_path)
    X_new = transform_new_data(df_new, feature_encoders)
    y_pred_encoded = oner_model.predict(X_new)
    y_pred = target_encoder.inverse_transform(y_pred_encoded)
    results = df_new.copy()
    results['1R_prediction'] = y_pred
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict_1R.py <path_to_new_csv>")
        sys.exit(1)
    predictions = predict_1R(sys.argv[1])
    print(predictions)