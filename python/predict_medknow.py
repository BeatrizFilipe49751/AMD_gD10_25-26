import sys
import numpy as np
import pandas as pd
from utils import load_models
from config import ID3_MODEL_PATH, NB_MODEL_PATH, FEATURE_ENCODERS_PATH, TARGET_ENCODER_PATH

def predict_new_data(id3_path, nb_path, feature_encoders_path, target_encoder_path, input_csv_path):
    id3_model, nb_model, feature_encoders, target_encoder = load_models(
        id3_path, nb_path, feature_encoders_path, target_encoder_path
    )

    df_new = pd.read_csv(input_csv_path)
    X_new = transform_new_data(df_new, feature_encoders)

    y_pred_id3_encoded = id3_model.predict(X_new)
    y_pred_nb_encoded = nb_model.predict(X_new)

    y_pred_id3 = target_encoder.inverse_transform(y_pred_id3_encoded)
    y_pred_nb = target_encoder.inverse_transform(y_pred_nb_encoded)

    results = df_new.copy()
    results['ID3_prediction'] = y_pred_id3
    results['NB_prediction'] = y_pred_nb

    return results


def transform_new_data(df: pd.DataFrame, feature_encoders: dict) -> pd.DataFrame:
    """Apply saved encoders to new data (same logic as training preprocessing)."""
    X_new = df.copy()

    # Fill missing categorical values
    for col in X_new.select_dtypes(include=['object', 'category']).columns:
        X_new[col] = X_new[col].fillna('none')

    # Apply encoders
    for col, encoder in feature_encoders.items():
        if col in X_new.columns:
            X_new[col] = X_new[col].apply(lambda val: val if val in encoder.classes_ else 'none')
            if 'none' not in encoder.classes_:
                encoder.classes_ = np.append(encoder.classes_, 'none')
            X_new[col] = encoder.transform(X_new[col])

    return X_new


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict_new_data.py <path_to_new_csv>")
        sys.exit(1)

    input_csv_path = sys.argv[1]

    predictions = predict_new_data(
        ID3_MODEL_PATH,
        NB_MODEL_PATH,
        FEATURE_ENCODERS_PATH,
        TARGET_ENCODER_PATH,
        input_csv_path
    )

    print(predictions)