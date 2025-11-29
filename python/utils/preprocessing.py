import re
from typing import Tuple
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split


def preprocess_data(df: pd.DataFrame, target_column: str, split=True) -> Tuple[pd.DataFrame, pd.Series, dict, LabelEncoder]:
    """
    Preprocess the dataset by encoding categorical features and the target variable,
    and splitting the data into training and testing sets.

    Steps:
        1. Separate the features (X) from the target (y).
        2. Fill missing values in categorical columns with 'none'.
        3. Encode all categorical features numerically using LabelEncoder.
        4. Encode the target column.
        5. Split the dataset into train/test subsets for evaluation.

    Returns:
        X_train (pd.DataFrame): Encoded training features
        X_test (pd.DataFrame): Encoded testing features
        y_train (pd.Series): Encoded training labels
        y_test (pd.Series): Encoded testing labels
        feature_encoders (dict): Dictionary mapping feature names → LabelEncoder objects
        target_encoder (LabelEncoder): Encoder fitted on the target column
    """
    # --- 1. Remove rows with invalid target ---
    df = df[df[target_column].apply(is_valid_value)]

    # --- 1. Separate features and target ---
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # --- 2. Handle missing values ---
    for col in X.select_dtypes(include=['object', 'category']).columns: 
        X[col] = X[col].fillna('none')

    # --- 3. Encode all categorical feature columns ---
    X_encoded, feature_encoders = encode_features(X)

    # --- 4. Encode the target column ---
    y_encoded, target_encoder = encode_target(y)
    
    if split:
        # --- 5. Split into training and testing sets ---
        X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.3, random_state=42)
        return X_train, X_test, y_train, y_test, feature_encoders, target_encoder
    else:
        return X_encoded, y_encoded, feature_encoders, target_encoder

def is_valid_value(val: str) -> bool:
    """Check if the value contains at least one alphanumeric character."""
    return bool(re.search(r"\w", str(val)))


def encode_target(y: pd.Series) -> Tuple[pd.Series, LabelEncoder]:
    """
    Label-encode the target variable (convert string labels to integers).
    Example: ['hard', 'soft', 'none'] → [0, 1, 2]

    Returns:
        y_encoded (pd.Series): Encoded target as integers
        le (LabelEncoder): The fitted encoder (for decoding later)
    """
    le = LabelEncoder()
    # Ensure target values are treated as strings before encoding
    y_encoded = le.fit_transform(y.astype(str))
    return y_encoded, le


def encode_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
    """
    Encode all categorical (non-numeric) feature columns using LabelEncoder.
    Each column gets its own encoder so that future transformations remain consistent.

    Returns:
        df_encoded (pd.DataFrame): Copy of df with all categorical columns replaced by integer codes
        encoders (dict): Dictionary of column name → fitted LabelEncoder
    """
    # Identify categorical feature columns (object or category dtype)
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    encoders = {}
    df_encoded = df.copy()

    # Encode each categorical feature independently
    for col in categorical_cols:
        le = LabelEncoder()
        # Convert to string to avoid issues with mixed types
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
        encoders[col] = le  # Store encoder for future decoding

    return df_encoded, encoders