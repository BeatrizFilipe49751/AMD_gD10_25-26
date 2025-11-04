from sklearn.tree import DecisionTreeClassifier
import pandas as pd


def train_id3(X_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
    """
    Train an ID3 Decision Tree classifier.
    This function uses scikit-learn's `DecisionTreeClassifier` with the
    information gain criterion ('entropy') to replicate the ID3 algorithm.
    Args:
        X_train (pd.DataFrame): Encoded training features.
        y_train (pd.Series): Encoded target labels.

    Returns:
        DecisionTreeClassifier: Trained ID3 model ready for predictions.
    """
    # Initialize the ID3 model using entropy as the split criterion
    id3_model = DecisionTreeClassifier(criterion='entropy')

    # Train the model on the training dataset
    id3_model.fit(X_train, y_train)

    # Return the trained model
    return id3_model
