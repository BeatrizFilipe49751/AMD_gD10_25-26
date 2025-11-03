import pandas as pd
from sklearn.naive_bayes import CategoricalNB

def train_nb(X_train: pd.DataFrame, y_train: pd.Series) -> CategoricalNB:
    """
    Train a Naive Bayes classifier using LabelEncoder for features and target.

    Returns:
        model: trained CategoricalNB model
    """
    # Create and train Naive Bayes model
    nb_model = CategoricalNB()
    nb_model.fit(X_train, y_train)
    return nb_model
