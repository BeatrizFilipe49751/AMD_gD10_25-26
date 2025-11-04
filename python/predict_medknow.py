import sys
import numpy as np
import pandas as pd
from load_models import load_models
import config

def predict_new_data(oner_path: str, id3_path: str, nb_path: str, feature_encoders_path: str, 
                     target_encoder_path: str, input_csv_path: str) -> pd.DataFrame:
    """
    Load pre-trained models and encoders, apply them to new data, and generate predictions.

    Steps:
        1. Load saved models (1R, ID3, Naive Bayes) and encoders.
        2. Preprocess and encode new input data using saved feature encoders.
        3. Generate predictions from all models.
        4. Decode predictions back to original label format.
        5. Return a DataFrame combining input data and model predictions.
        
    Returns:
        pd.DataFrame: DataFrame containing the input data with added prediction columns.
    """
    # Load all saved models and encoders
    oner_model, id3_model, nb_model, feature_encoders, target_encoder = load_models(
        oner_path, id3_path, nb_path, feature_encoders_path, target_encoder_path
    )

    # Load and preprocess new data
    df_new = pd.read_csv(input_csv_path)
    X_new = transform_new_data(df_new, feature_encoders)

    # --- Generate encoded predictions for each model ---
    y_pred_1r_encoded = oner_model.predict(X_new)
    y_pred_id3_encoded = id3_model.predict(X_new)
    y_pred_nb_encoded = nb_model.predict(X_new)

    # --- Decode predictions back to original label values ---
    y_pred_1r = target_encoder.inverse_transform(y_pred_1r_encoded)
    y_pred_id3 = target_encoder.inverse_transform(y_pred_id3_encoded)
    y_pred_nb = target_encoder.inverse_transform(y_pred_nb_encoded)

    # Combine predictions with the original input data
    results = df_new.copy()
    results['1R_prediction'] = y_pred_1r
    results['ID3_prediction'] = y_pred_id3
    results['NB_prediction'] = y_pred_nb

    return results


def transform_new_data(df: pd.DataFrame, feature_encoders: dict) -> pd.DataFrame:
    """
    Apply saved encoders to transform new data into the same encoded format as training data.

    Steps:
        1. Fill missing categorical values with 'none'.
        2. Use stored LabelEncoders to transform categorical columns.
        3. Handle unseen values by mapping them to 'none'.

    Args:
        df (pd.DataFrame): New data to be transformed.
        feature_encoders (dict): Dictionary mapping column names to LabelEncoders.

    Returns:
        pd.DataFrame: Encoded feature DataFrame ready for prediction.
    """
    X_new = df.copy()

    # Fill missing categorical values with 'none'
    for col in X_new.select_dtypes(include=['object', 'category']).columns:
        X_new[col] = X_new[col].fillna('none')

    # Encode features using stored LabelEncoders
    for col, encoder in feature_encoders.items():
        if col in X_new.columns:
            # Handle unseen categorical values by replacing them with 'none'
            X_new[col] = X_new[col].apply(lambda val: val if val in encoder.classes_ else 'none')
            
            # Ensure 'none' is part of encoder classes
            if 'none' not in encoder.classes_:
                encoder.classes_ = np.append(encoder.classes_, 'none')
                
            # Apply encoding
            X_new[col] = encoder.transform(X_new[col])

    return X_new


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict_new_data.py <path_to_new_csv>")
        sys.exit(1)

    input_csv_path = sys.argv[1]

    predictions = predict_new_data(
        config.ONER_MODEL_PATH,
        config.ID3_MODEL_PATH,
        config.NB_MODEL_PATH,
        config.FEATURE_ENCODERS_PATH,
        config.TARGET_ENCODER_PATH,
        input_csv_path
    )

    print(predictions)