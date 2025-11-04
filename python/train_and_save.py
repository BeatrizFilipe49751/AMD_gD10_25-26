import pickle
import sys
import pandas as pd
# Import model training functions
from models.train_id3 import train_id3
from models.train_nb import train_nb
from models.one_rule import OneRuleClassifier
# Import preprocessing and configuration paths
from preprocessing import preprocess_data
import config


def train_and_save_models(dataset_path: str, target_column: str):
    """
    Train multiple models (1R, ID3, Naive Bayes) and save them along with their encoders and test data.
    
    Steps:
    1. Load the dataset and preprocess it (encoding categorical features/target).
    2. Train the following models:
        - One Rule (1R)
        - ID3 Decision Tree
        - Naive Bayes
    3. Save trained models, encoders, and test sets as pickled files or CSVs.

    Args:
        dataset_path: Path to the CSV dataset file.
        target_column: Name of the target variable in the dataset.
    """
    # --- Step 1: Load and preprocess dataset ---
    df = pd.read_csv(dataset_path)
    X_train, X_test, y_train, y_test, feature_encoders, target_encoder = preprocess_data(df, target_column)
    
    # --- Step 2: Train models ---
    # Train our 1R model
    oner_model = OneRuleClassifier().fit(X_train, y_train)
    
    # Train ID3 model
    id3_model = train_id3(X_train, y_train)
    
    # Train Naive Bayes model
    nb_model = train_nb(X_train, y_train)
    
    # --- Step 3: Save data and models ---
    
    # --- Save test sets as CSV ---
    X_test.to_csv(config.X_TEST_PATH, index=False)
    pd.Series(y_test).to_csv(config.Y_TEST_PATH, index=False, header=False)
    
    # --- Save encoders ---
    with open(config.FEATURE_ENCODERS_PATH, "wb") as f:
        pickle.dump(feature_encoders, f)
    with open(config.TARGET_ENCODER_PATH, "wb") as f:
        pickle.dump(target_encoder, f)
    
    # --- Save models ---
    with open(config.ONER_MODEL_PATH, "wb") as f:
        pickle.dump(oner_model, f)
    with open(config.ID3_MODEL_PATH, "wb") as f:
        pickle.dump(id3_model, f)
    with open(config.NB_MODEL_PATH, "wb") as f:
        pickle.dump(nb_model, f)
    
    print("Models, encoders, and test sets saved successfully.")

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python train_and_save.py <target_column> [optional: <dataset_path>]")
        sys.exit(1)

    target_column = sys.argv[1]
    dataset_path = sys.argv[2] if len(sys.argv) > 2 else config.DATASET_PATH

    train_and_save_models(dataset_path, target_column)