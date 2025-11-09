import pandas as pd
import sys
from ..utils.transform_new_data import transform_new_data
from ..utils.load_models import load_id3_nb, load_encoders


def predict_classifiers(input_csv_path: str) -> pd.DataFrame:
    id3_model, nb_model = load_id3_nb()
    feature_encoders, target_encoder = load_encoders()

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict_classifiers.py <path_to_new_csv>")
        sys.exit(1)
    predictions = predict_classifiers(sys.argv[1])
    print(predictions)