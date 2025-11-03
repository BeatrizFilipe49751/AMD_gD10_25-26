import os

# Go one directory up from /python to reach project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define subdirectories relative to the project root
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
DATASETS_DIR = os.path.join(BASE_DIR, "scripts/datasets")

# Files
ID3_MODEL_PATH = os.path.join(ARTIFACTS_DIR, "id3_model.pkl")
NB_MODEL_PATH = os.path.join(ARTIFACTS_DIR, "nb_model.pkl")
FEATURE_ENCODERS_PATH = os.path.join(ARTIFACTS_DIR, "feature_encoders.pkl")
TARGET_ENCODER_PATH = os.path.join(ARTIFACTS_DIR, "target_encoder.pkl")
X_TEST_PATH = os.path.join(ARTIFACTS_DIR, "X_test.csv")
Y_TEST_PATH = os.path.join(ARTIFACTS_DIR, "y_test.csv")
DATASET_PATH = os.path.join(DATASETS_DIR, "dataset.csv")