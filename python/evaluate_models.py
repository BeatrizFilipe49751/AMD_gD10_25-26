import time
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
from .utils.load_models import load_1R, load_id3_nb, load_encoders
from .utils import config

def evaluate_models(oner_model, id3_model, nb_model, target_encoder, X_test_path: str, y_test_path: str) -> None:
    """
    Evaluate and compare multiple trained models (1R, ID3, and Naive Bayes).

    Steps:
        1. Load test data from CSV files.
        2. Decode target labels from their encoded form.
        3. Generate predictions and measure execution time for each model.
        4. Compute metrics (accuracy, confusion matrix, classification report).
        5. Summarize results to identify the best and fastest models.
    """
    # Load test data
    X_test = pd.read_csv(X_test_path)
    y_test = pd.read_csv(y_test_path, header=None).squeeze()
    
    # Decode true labels (from numeric back to original categories)
    y_true = target_encoder.inverse_transform(y_test)

    # --- Generate predictions and measure execution time for each model ---
    start_time_id3 = time.perf_counter()
    y_pred_id3 = id3_model.predict(X_test)
    elapsed_time_id3 = time.perf_counter() - start_time_id3
    
    start_time_nb = time.perf_counter()
    y_pred_nb = nb_model.predict(X_test)
    elapsed_time_nb = time.perf_counter() - start_time_nb
    
    start_time_1r = time.perf_counter()
    y_pred_1r = oner_model.predict(X_test)
    elapsed_time_1r = time.perf_counter() - start_time_1r

    # Decode model predictions back to original labels
    y_pred_id3 = target_encoder.inverse_transform(y_pred_id3)
    y_pred_nb = target_encoder.inverse_transform(y_pred_nb)
    y_pred_1r = target_encoder.inverse_transform(y_pred_1r)
    
    # --- Evaluate and store results for each model ---
    results = []
    results.append(evaluate_single_model("1R", y_true, y_pred_1r, elapsed_time_1r))
    results.append(evaluate_single_model("ID3", y_true, y_pred_id3, elapsed_time_id3))
    results.append(evaluate_single_model("Naive Bayes", y_true, y_pred_nb, elapsed_time_nb))

    # --- Display summary table ---
    summarize_results(results)


def evaluate_single_model(name: str, y_true: pd.Series, y_pred: pd.Series, elapsed_time: float) -> dict:
    """
    Evaluate a single model by computing metrics and printing results.

    Args:
        name (str): Name of the model (for display).
        y_true (pd.Series): True (decoded) labels.
        y_pred (pd.Series): Predicted (decoded) labels.
        elapsed_time (float): Execution time for generating predictions.

    Returns:
        dict: A dictionary with model name, accuracy, and elapsed time.
    """
    acc = accuracy_score(y_true, y_pred)

    print(f"\n=== {name} Evaluation ===")
    print(f"Accuracy: {acc:.4f}")
    print(f"Execution Time: {elapsed_time:.6f} seconds")
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred, zero_division=0))

    return {"Model": name, "Accuracy": acc, "Time (s)": elapsed_time}


def summarize_results(results: list[dict]) -> None:
    """
    Summarize all model evaluations, showing accuracy and execution time.

    Args:
        results (list[dict]): List of dictionaries with model results.
    """
    df_results = pd.DataFrame(results)
    print("\n=== Summary of Model Evaluations ===")
    print(df_results.sort_values(by=["Accuracy", "Time (s)"], ascending=[False, True]).to_string(index=False))

    # Determine best model(s) by accuracy
    best_acc = df_results["Accuracy"].max()
    best_models = df_results[df_results["Accuracy"] == best_acc]["Model"].tolist()

    if len(best_models) > 1:
        print(f"\nBest models: {', '.join(best_models)} (Accuracy = {best_acc:.4f})")
    else:
        print(f"\nBest Model: {best_models[0]} (Accuracy = {best_acc:.4f})")

    # Identify the fastest model by lowest execution time
    fastest = df_results.loc[df_results["Time (s)"].idxmin()]
    print(f"Fastest Model: {fastest['Model']} (Time = {fastest['Time (s)']:.6f}s)")


if __name__ == "__main__":
    oner_model = load_1R() 
    id3_model, nb_model = load_id3_nb()
    feature_encoders, target_encoder = load_encoders()
    evaluate_models(oner_model, id3_model, nb_model, target_encoder, config.X_TEST_PATH, config.Y_TEST_PATH)