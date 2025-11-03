import pickle
import pandas as pd
from train_id3 import train_id3
from train_nb import train_nb
from preprocessing import preprocess_data
from config import ID3_MODEL_PATH, NB_MODEL_PATH, FEATURE_ENCODERS_PATH, TARGET_ENCODER_PATH, X_TEST_PATH, Y_TEST_PATH, DATASET_PATH

def train_and_save_models(dataset_path: str, target_column: str):
    df = pd.read_csv(dataset_path)
    
    # Preprocess the data
    X_train, X_test, y_train, y_test, feature_encoders, target_encoder = preprocess_data(df, target_column)
    
    # Train ID3 model
    id3_model = train_id3(X_train, y_train)
    
    # Train Naive Bayes model
    nb_model = train_nb(X_train, y_train)
    
    # --- Save test sets as CSV ---
    X_test.to_csv(X_TEST_PATH, index=False)
    pd.Series(y_test).to_csv(Y_TEST_PATH, index=False, header=False)
    
    # --- Save encoders ---
    with open(FEATURE_ENCODERS_PATH, "wb") as f:
        pickle.dump(feature_encoders, f)
    with open(TARGET_ENCODER_PATH, "wb") as f:
        pickle.dump(target_encoder, f)
    
    # --- Save models ---
    with open(ID3_MODEL_PATH, "wb") as f:
        pickle.dump(id3_model, f)
    with open(NB_MODEL_PATH, "wb") as f:
        pickle.dump(nb_model, f)
    
    print("Models, encoders, and test sets saved successfully.")

    
if __name__ == "__main__":
    train_and_save_models(DATASET_PATH, target_column="lenses")