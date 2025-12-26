import pandas as pd
from sklearn.naive_bayes import CategoricalNB


def train_nb(X_train: pd.DataFrame, y_train: pd.Series) -> CategoricalNB:
    """
    Train a Naive Bayes classifier for categorical data.
    This function uses scikit-learn's `CategoricalNB`, which is designed for
    datasets where all features are discrete or encoded as integers.
    Args:
        X_train (pd.DataFrame): Encoded training feature set.
        y_train (pd.Series): Encoded target labels.

    Returns:
        CategoricalNB: Trained Naive Bayes model.
    """
    # Initialize a Naive Bayes model for categorical features
    nb_model = CategoricalNB()

    # Train the model on the training dataset
    nb_model.fit(X_train, y_train)

    # Return the trained model
    return nb_model