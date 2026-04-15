import pandas as pd
import joblib
import os
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score


def test_model(test_path, model_path, algo_type):
    """
    PURPOSE: Comprehensive Performance Auditing (Slide 75).

    This function acts as a 'Scientific Auditor'. It evaluates the serialized
    model artifacts against unseen test folds to ensure 'Out-of-Sample' integrity.
    It extracts granular metrics (TP, FP, TN, FN) and harmonic balances (F1-Score)
    to defend the model's strategic value beyond simple accuracy.

    ARGUMENTS:
    - test_path: Path to the unseen CSV fold.
    - model_path: Path to the serialized .pkl artifact.
    - algo_type: Identifier for logic branch (ALGO01 for Heuristic, ALGO02 for ML).
    """

    # 1. ARTIFACT & DATA RECOVERY
    artifact = joblib.load(model_path)
    test_df = pd.read_csv(test_path)
    y_true = test_df['PERCEIVED_AGE']

    # 2. INFERENCE LOGIC (Slide 4: Anti-Self-Deception)
    if algo_type == "ALGO01":
        # NAIVE HEURISTIC: Applying biological age rules
        predictions = []
        limits = artifact['thresholds']
        for age in test_df['AGE']:
            if age < limits['young_limit']:
                predictions.append("YOUNG_ADULT")
            elif age < limits['adult_limit']:
                predictions.append("ADULT")
            else:
                predictions.append("OLD")
    else:
        # ML ENGINE: Re-aligning features to match training state
        model = artifact['model_object']
        features = artifact['feature_names']

        X_test = test_df.drop(columns=['PERSON_ID', 'AGE', 'PERCEIVED_AGE'])
        X_test = pd.get_dummies(X_test).reindex(columns=features, fill_value=0)
        predictions = model.predict(X_test)

    # 3. MULTI-CLASS METRIC EXTRACTION (Slide 75: Decision Defense)
    # Core Metric: Accuracy
    acc = accuracy_score(y_true, predictions)

    # Harmonic Metrics: Using 'macro' average to treat all classes equally
    # Precision: The ability not to label a negative sample as positive.
    # Recall: The ability to find all positive samples.
    precision = precision_score(y_true, predictions, average='macro', zero_division=0)
    recall = recall_score(y_true, predictions, average='macro', zero_division=0)
    f1 = f1_score(y_true, predictions, average='macro', zero_division=0)

    # 4. CONFUSION MATRIX DECOMPOSITION
    # Classes must be explicit to ensure consistent matrix dimensions (3x3)
    labels = ["YOUNG_ADULT", "ADULT", "OLD"]
    cm = confusion_matrix(y_true, predictions, labels=labels)

    # Mathematical Decomposition for the Ledger:
    tp_total = np.diag(cm).sum()  # Sum of diagonal elements (Correct Predictions)
    fp_total = cm.sum(axis=0).sum() - tp_total  # Predicted positives that are wrong
    fn_total = cm.sum(axis=1).sum() - tp_total  # Actual positives that were missed

    # TN calculation in Multi-class: Everything else that was correctly rejected
    # (Total instances * Class count) - (Other metrics)
    tn_total = (cm.sum() * len(labels)) - (tp_total + fp_total + fn_total)

    return acc, int(tp_total), int(fp_total), int(tn_total), int(fn_total), precision, recall, f1


def add_ledger_entry(ledger_path, timestamp, run_id, fold_id, algo, model_type, acc, tp, fp, tn, fn, prec, rec, f1, duration, seed):
    """
    Finalizes the audit by recording performance, cost (duration), and setup (seed).
    """
    with open(ledger_path, 'a') as f:
        entry = [
            str(timestamp), str(run_id), str(fold_id), str(algo), str(model_type),
            f"{acc:.4f}", str(tp), str(fp), str(tn), str(fn),
            f"{prec:.4f}", f"{rec:.4f}", f"{f1:.4f}",
            f"{duration:.6f}", str(seed)
        ]
        f.write(",".join(entry) + "\n")
