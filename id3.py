import math

# ------------------------------
# Helper Functions
# ------------------------------

def get_subset(data, attribute, value):
    """
    Returns a subset of the dataset where the specified attribute has the given value.

    Parameters:
        data      : pandas DataFrame
        attribute : name of the column to filter
        value     : value of the attribute to match

    Returns:
        pandas DataFrame : subset of data matching the condition
    """
    return data[data[attribute] == value]


def calculate_entropy(data, target):
    """
    Calculates the entropy of the target column in the dataset.

    Entropy measures the amount of uncertainty/impurity in the target.
    Formula: H(S) = - Σ p_i * log2(p_i), for all classes i in the target

    Parameters:
        data   : pandas DataFrame
        target : name of the target column

    Returns:
        float : entropy value
    """
    rows = len(data)
    values = data[target].unique()
    entropy = 0.0
    for value in values:
        count = sum(data[target] == value) # Count occurrences of each class value
        frequency = count / rows # Probability of this class value
        if frequency > 0:
            entropy += frequency * math.log2(frequency)
    return -entropy


def calculate_information_gain(data, attribute, target):
    """
    Calculates the information gain of splitting the dataset on a given attribute.

    Information Gain = Entropy(dataset) - Σ (proportion of subset) * Entropy(subset)

    Parameters:
        data      : pandas DataFrame
        attribute : column name to calculate information gain
        target    : name of the target column

    Returns:
        float : information gain value
    """
    dataset_entropy = calculate_entropy(data, target)
    values = data[attribute].unique()
    subset_entropy = 0.0
    for value in values:
        subset = get_subset(data, attribute, value)
        frequency = len(subset) / len(data)
        subset_entropy += frequency * calculate_entropy(subset, target)
    information_gain = dataset_entropy - subset_entropy
    return information_gain


def get_all_info_gains(data, attributes, target):
    """
    Calculates the information gain for all attributes (except the target).

    Parameters:
        data       : pandas DataFrame
        attributes : list of attribute names
        target     : name of the target column

    Returns:
        dict : mapping of attribute -> information gain
    """
    info_gains = {}
    for attribute in attributes:
        if attribute != target:
            info_gains[attribute] = calculate_information_gain(data, attribute, target)
    return info_gains


def select_best_attribute(data, info_gains):
    """
    Selects the best attribute to split on, choosing the one with the highest information gain.
    If there is a tie, selects the attribute with less unique values (less branches).

    Parameters:
        data       : pandas DataFrame
        info_gains : dict of attribute -> information gain

    Returns:
        str : name of the best attribute
    """
    best_attribute = max(info_gains, key=lambda k: (info_gains[k], -len(data[k].unique())))
    return best_attribute


# ------------------------------
# ID3 Algorithm
# ------------------------------

def id3(data, attributes, target):
    """
    Recursively builds a decision tree using the ID3 algorithm.

    Base cases:
        1. If no attributes left, return the class with highest frequency
        2. If every row in the current subset has the same value for the target column - 
        there is no uncertainty, return that class as the leaf node

    Recursive case:
        1. Calculate information gain for all attributes
        2. Select attribute with highest gain as the decision node
        3. For each value of this attribute, create a branch with a subtree

    Parameters:
        data       : pandas DataFrame
        attributes : list of attribute names to consider for splitting
        target     : name of the target column

    Returns:
        dict or str : decision tree represented as nested dictionaries, 
                      with leaves as class labels
    """
    # Base case 1
    if len(attributes) == 0:
        return data[target].mode()[0] # most frequent value in target column
    
    # Base case 2
    unique_values = data[target].unique()
    if len(unique_values) == 1:
        return unique_values[0] # all rows have the same target value
    
    info_gains = get_all_info_gains(data, attributes, target)
    best_attribute = select_best_attribute(data, info_gains)
    
    # Remove the chosen attribute from future splits
    attributes.remove(best_attribute)
    
    # Create the tree node
    tree = {best_attribute: {}}
    
    # Create a subtree for each value of the attribute
    values = data[best_attribute].unique()
    for value in values:
        subset = get_subset(data, best_attribute, value)
        tree[best_attribute][value] = id3(subset, attributes.copy(), target)
    return tree