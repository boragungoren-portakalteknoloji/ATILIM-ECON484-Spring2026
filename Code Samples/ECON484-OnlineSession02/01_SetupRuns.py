import pandas as pd
import os
import datetime
from sklearn.model_selection import KFold
from sklearn.utils import shuffle


# --- STEP 1: Setup the Environment (Slide 3: Lab Notebook) ---
def create_experiment_assets(raw_data_path):
    """
    Creates the physical folder structure for a new 'Run'.
    Returns the paths for folds, models, and the ledger file.
    """
    # Generate a unique timestamp-based ID for the run
    run_id = datetime.datetime.now().strftime("run_%Y%m%d_%H%M%S")
    base_dir = os.path.join("Experiments", run_id)

    # Define sub-directories
    folds_dir = os.path.join(base_dir, "Folds")
    models_dir = os.path.join(base_dir, "Models")
    ledger_file = os.path.join(base_dir, "ledger.csv")

    # Create directories physically (Slide 3: Immutable Record)
    os.makedirs(folds_dir, exist_ok=False)
    os.makedirs(models_dir, exist_ok=False)

    print(f"[STATUS] Environment created at: {base_dir}")
    return run_id, folds_dir, models_dir, ledger_file


# --- STEP 2: Initialize the Ledger (Slide 72: Accountability) ---
def initialize_ledger(ledger_path):
    """
    Creates the ledger file with headers.
    """
    headers = [
        "Timestamp", "Run_ID", "Fold_ID", "Algorithm", "Model_File",
        "Accuracy", "TP", "FP", "TN", "FN", "Precision", "Recall", "F1_Score",
        "Train_Duration", "Seed"
    ]
    # Create an empty DataFrame and save it as CSV
    df = pd.DataFrame(columns=headers)
    df.to_csv(ledger_path, index=False)
    print(f"[STATUS] Ledger initialized at: {ledger_path}")


# --- STEP 3: Execute Shuffling and Splitting (Slide 4: Reproducibility) ---
def split_and_save_data(raw_data_path, folds_dir, n_splits=10, seed=42):
    """
    Reads the raw data, shuffles it, and writes K-Fold CSVs to disk.
    """
    # Load raw data
    data = pd.read_csv(raw_data_path)

    # Shuffle the data (Anti-Self-Deception)
    # Using a fixed seed ensures we can get the same results tomorrow.
    data_shuffled = shuffle(data, random_state=seed)

    # K-Fold logic
    kf = KFold(n_splits=n_splits, shuffle=False)

    print(f"[STATUS] Starting K-Fold split (N={n_splits})...")

    fold_counter = 1
    for train_index, test_index in kf.split(data_shuffled):
        train_set = data_shuffled.iloc[train_index]
        test_set = data_shuffled.iloc[test_index]

        # Define file names
        train_name = f"train_{fold_counter:03d}.csv"
        test_name = f"test_{fold_counter:03d}.csv"

        # Save to disk
        train_set.to_csv(os.path.join(folds_dir, train_name), index=False)
        test_set.to_csv(os.path.join(folds_dir, test_name), index=False)

        fold_counter += 1

    print(f"[SUCCESS] All {n_splits} folds are saved in {folds_dir}")


# RAW_DATA = "./Raw Data/labeled_data.csv"
# N_FOLDS = 10
# RANDOM_SEED = 42

# 1. Start the provisioning process
# run_id, f_dir, m_dir, l_file = create_experiment_assets(RAW_DATA)

# 2. Setup the record keeping
# initialize_ledger(l_file)

# 3. Physically split the data
# split_and_save_data(RAW_DATA, f_dir, n_splits=N_FOLDS, seed=RANDOM_SEED)