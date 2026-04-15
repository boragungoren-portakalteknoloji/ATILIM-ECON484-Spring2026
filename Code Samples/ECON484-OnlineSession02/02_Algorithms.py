import pandas as pd
import joblib  # Standard tool for serializing Python objects
import os
from sklearn.tree import DecisionTreeClassifier

# --- ALGO 01: The Naive Baseline Trainer (Slide 74) ---
def train_algo_01(train_path, model_output_path):
    """
    PURPOSE:
    To establish a 'Baseline' (Naive Forecast) using biological age rules.
    In ML, we must always prove that our complex models perform better
    than a simple human-defined rule.

    LOGIC:
    This function does not 'learn' from data. Instead, it creates a
    dictionary of thresholds based on common sense:
    - YOUNG_ADULT: Age < 35
    - ADULT: Age 35 to 55
    - OLD: Age > 55

    INPUT:
    - train_path: Path to the current fold's training CSV.
    - model_output_path: Destination for the .pkl artifact.
    """
    print(f"[ALGO 01] Generating Naive Baseline for: {os.path.basename(train_path)}")

    # Static logic based on the 'AGE' column
    naive_logic = {
        "metadata": "Static rule-based heuristic on biological age",
        "thresholds": {
            "young_limit": 35,
            "adult_limit": 55
        },
        "classes": ["YOUNG_ADULT", "ADULT", "OLD"]
    }

    # Serialize the rules to disk to maintain the system pipeline
    joblib.dump(naive_logic, model_output_path)
    print(f"[ALGO 01] Baseline saved: {model_output_path}")


# --- ALGO 02: The Decision Tree Trainer (Slide 46) ---
def train_algo_02(train_path, model_output_path):
    """
    PURPOSE:
    To train a machine learning model (Decision Tree) that discovers
    patterns between digital exhaustion (Email/DM intensity) and
    perceived age, without knowing the person's true biological age.

    LOGIC:
    - Feature Isolation: Explicitly removes 'AGE' to prevent 'Data Leakage'.
    - Categorical Encoding: Converts 'ROLE' and 'SENIORITY' into numeric
      dummy variables (One-Hot Encoding) so the math works.
    - Model Fit: Uses a depth-constrained Decision Tree to prevent overfitting.

    INPUT:
    - train_path: Path to the current fold's training CSV.
    - model_output_path: Destination for the .pkl artifact.
    """
    print(f"[ALGO 02] Training ML Model for: {os.path.basename(train_path)}")

    # Load the training data
    train_df = pd.read_csv(train_path)

    # 1. Feature Selection (Slide 4: Anti-Self-Deception)
    # We drop 'PERSON_ID' (noise) and 'AGE' (to ensure an honest test).
    # 'PERCEIVED_AGE' is our target variable (Label).
    X = train_df.drop(columns=['PERSON_ID', 'AGE', 'PERCEIVED_AGE'])
    y = train_df['PERCEIVED_AGE']

    # 2. Preprocessing: Handle categorical text data
    X_encoded = pd.get_dummies(X)

    # 3. Training the Artifact
    # Constraining max_depth=5 keeps the model 'simple' and interpretable.
    clf = DecisionTreeClassifier(max_depth=5, random_state=42)
    clf.fit(X_encoded, y)

    # 4. Save the model and the feature names together
    # We save the features to ensure the Tester uses the same columns later.
    artifact = {
        "model_object": clf,
        "feature_names": X_encoded.columns.tolist(),
        "algorithm_type": "Decision Tree Classifier"
    }

    joblib.dump(artifact, model_output_path)
    print(f"[ALGO 02] ML Artifact saved: {model_output_path}")