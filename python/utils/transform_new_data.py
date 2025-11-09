import pandas as pd
import numpy as np


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