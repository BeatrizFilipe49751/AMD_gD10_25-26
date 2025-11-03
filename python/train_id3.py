from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def train_id3(X_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeClassifier:
    """
    Train an ID3 Decision Tree classifier using LabelEncoder for features and target.

    Returns:
        model: trained DecisionTreeClassifier
    """
    # Create and train ID3 model
    id3_model = DecisionTreeClassifier(criterion='entropy')
    id3_model.fit(X_train, y_train)
    return id3_model