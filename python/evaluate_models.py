from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
from utils import load_models
from config import ID3_MODEL_PATH, NB_MODEL_PATH, FEATURE_ENCODERS_PATH, TARGET_ENCODER_PATH, X_TEST_PATH, Y_TEST_PATH

def evaluate_models(id3_model, nb_model, target_encoder, X_test_path: str, y_test_path: str):
    # Load test data
    X_test = pd.read_csv(X_test_path)
    y_test = pd.read_csv(y_test_path, header=None).squeeze()

    # Predictions
    y_pred_id3 = id3_model.predict(X_test)
    y_pred_nb = nb_model.predict(X_test)

    # Decode predictions if target was encoded
    y_pred_id3 = target_encoder.inverse_transform(y_pred_id3)
    y_pred_nb = target_encoder.inverse_transform(y_pred_nb)
    y_true = target_encoder.inverse_transform(y_test)

    print("=== ID3 Evaluation ===")
    print("Accuracy:", accuracy_score(y_true, y_pred_id3))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred_id3))
    print("Classification Report:\n", classification_report(y_true, y_pred_id3))

    print("\n=== Naive Bayes Evaluation ===")
    print("Accuracy:", accuracy_score(y_true, y_pred_nb))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred_nb))
    print("Classification Report:\n", classification_report(y_true, y_pred_nb))


if __name__ == "__main__":
    id3_model, nb_model, feature_encoders, target_encoder = load_models(
        ID3_MODEL_PATH, NB_MODEL_PATH, FEATURE_ENCODERS_PATH, TARGET_ENCODER_PATH)

    evaluate_models(id3_model, nb_model, target_encoder, X_TEST_PATH, Y_TEST_PATH)