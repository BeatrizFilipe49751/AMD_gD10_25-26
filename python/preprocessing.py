from typing import Tuple
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(df: pd.DataFrame, target_column: str) -> Tuple[pd.DataFrame, pd.Series, dict, LabelEncoder]:
    """
    Preprocess the dataset by encoding categorical features and the target variable.

    Returns:
        X_encoded: DataFrame with encoded features
        y_encoded: Series with encoded target
        feature_encoders: dict of column -> LabelEncoder for features
        target_encoder: LabelEncoder for the target
    """
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Fill missing values in all categorical columns 
    for col in X.select_dtypes(include=['object', 'category']).columns: 
        X[col] = X[col].fillna('none')

    # Encode features
    X_encoded, feature_encoders = encode_features(X)

    # Encode target
    y_encoded, target_encoder = encode_target(y)
    
    # Split the dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test, feature_encoders, target_encoder


def encode_target(y: pd.Series) -> Tuple[pd.Series, LabelEncoder]:
    """
    Label-encode the target variable.
    
    Returns:
        y_encoded: encoded target
        le: LabelEncoder
    """
    le = LabelEncoder()
    y_encoded = le.fit_transform(y.astype(str))
    return y_encoded, le


def encode_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
    """
    Label-encode all categorical features in a DataFrame.
    
    Returns:
        df_encoded: DataFrame with encoded features
        encoders: dict of column -> LabelEncoder
    """
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    encoders = {}
    df_encoded = df.copy()

    for col in categorical_cols:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
        encoders[col] = le

    return df_encoded, encoders