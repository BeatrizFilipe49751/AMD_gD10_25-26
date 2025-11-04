from collections import defaultdict, Counter
from typing import Any, Dict, List
import pandas as pd


class OneRuleClassifier:
    """
    A self-contained 1R (One Rule) classifier.
    """
    def __init__(self):
        self.model_: Dict[str, Any] = {}
        self.trained_: bool = False

    def fit(self, X: pd.DataFrame, y: pd.Series):
        """
        Train the 1R model on the given dataset.

        Args:
            X (pd.DataFrame): Training features.
            y (pd.Series): Target variable.
        """
        df = X.copy()
        df["__target__"] = y
        self.model_ = train_one_rule(df.to_dict(orient="records"), "__target__")
        self.trained_ = True
        return self

    def predict(self, X: pd.DataFrame) -> pd.Series:
        """
        Predict labels using the trained model.
        Args:
            X (pd.DataFrame): Input features.

        Returns:
            pd.Series: Predicted labels.
        """
        if not self.trained_:
            raise RuntimeError("Model must be fitted before calling predict().")
        return predict_one_rule(self.model_, X)
    

def train_one_rule(train_rows: List[Dict[str, Any]], target: str) -> Dict[str, Any]:
    """
    Train a One Rule (1R) classifier.

    The 1R algorithm creates a simple rule based on a single feature — 
    the one that has the highest training accuracy. 
    For each possible value of that feature, the most frequent target 
    label is chosen as the prediction.
    Args:
        train_rows (List[Dict[str, Any]]): Training data as a list of dictionaries, 
            where each dict represents a row with feature-value pairs.
        target (str): The name of the target variable.

    Returns:
        Dict[str, Any]: A dictionary with:
            - 'feature': The best feature selected for the rule.
            - 'rule': A mapping of feature values → predicted class.
            - 'accuracy': The training accuracy of the selected rule.
    """
    # Get list of features except the target
    features = [f for f in train_rows[0] if f != target]

    best_attr, best_rule, best_acc = None, None, 0

    for attr in features:
        # Group target values by attribute value
        groups = defaultdict(list)
        for row in train_rows:
            groups[row[attr]].append(row[target])

        # Rule: for each attribute value, choose the most common class
        rule = {val: Counter(vals).most_common(1)[0][0] for val, vals in groups.items()}

        # Calculate accuracy on the training set
        correct = sum(1 for row in train_rows if rule.get(row[attr]) == row[target])
        acc = correct / len(train_rows)

        # Keep the best-performing feature and its rule
        if acc > best_acc:
            best_attr, best_rule, best_acc = attr, rule, acc

    return {"feature": best_attr, "rule": best_rule, "accuracy": best_acc}


def predict_one_rule(model: Dict[str, Any], X: pd.DataFrame) -> pd.Series:
    """
    Predict labels using a trained One Rule (1R) model.

    Each sample is classified based on the rule associated with the 
    selected feature. If the feature value wasn't seen during training, 
    a default class (the most common one) is used.
    Args:
        model (Dict[str, Any]): Trained 1R model.
        X (pd.DataFrame): Encoded test data.

    Returns:
        pd.Series: Predicted labels (encoded as integers).
    """
    feature = model['feature']
    rules = model['rule']

    # Precompute default target class: the most frequent predicted value
    default_target = next(iter(Counter(rules.values()).most_common(1)))[0]

    # Apply rules to feature values
    predictions = X[feature].replace(rules)
    
    # Fill unseen values with the default class
    predictions = predictions.where(predictions.notna(), default_target)

    return predictions.astype(int)