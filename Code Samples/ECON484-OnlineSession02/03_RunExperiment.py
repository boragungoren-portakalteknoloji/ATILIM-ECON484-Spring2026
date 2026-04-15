import os
import time
import importlib
from datetime import datetime
import time

# --- DYNAMIC IMPORTS (Slide 28: Automating Boilerplate) ---
setup_runs = importlib.import_module("01_SetupRuns")
model_trainer = importlib.import_module("02_Algorithms")
model_tester = importlib.import_module("02_Testers")

def main():
    """
    PURPOSE:
    Orchestrate the complete ML Lifecycle: Provisioning -> Training -> Testing -> Recording.

    STRATEGIC DEFENSE:
    Separates the 'Creation' of models from 'Evaluation' to ensure
    operational resilience and auditability.
    """

    print("\n" + "=" * 60)
    print("MASTER ORCHESTRATOR: END-TO-END EXPERIMENT ENGINE")
    print("=" * 60)

    RAW_DATA_PATH = "./Raw Data/labeled_data.csv"

    # Global Seed Control
    # Seed must be an int in the range [0, 4294967295]
    # Popular seeds include 42, 1234, 1337
    MY_SEED = 42

    # --- PHASE 1: PROVISIONING (The Infrastructure) ---
    try:
        # We create the experiement assets
        # We capture run_id, folds_dir, models_dir ve ledger_path as return variables
        run_id, f_dir, m_dir, l_file = setup_runs.create_experiment_assets(RAW_DATA_PATH)
        setup_runs.initialize_ledger(l_file)
        setup_runs.split_and_save_data(RAW_DATA_PATH, f_dir, n_splits=10, seed=MY_SEED)
    except FileExistsError:
        # if you have a system clock error or if you try to run the experiments too fast
        # this can happen. "too fast" means starting another experiment run within the same second.
        print("[CRITICAL] Run ID collision. Please check the system clock.")
        return

    # Listing the training files to be processed
    # Note that the model training data sets were created in the previous step and exist under Experiments
    train_files = sorted([f for f in os.listdir(f_dir) if f.startswith("train_")])
    train_metrics = {} # Dictionary

    # --- PHASE 2: EXECUTION - TRAINING (Creating the Brains) ---
    print(f"\n[PHASE 2] BATCH TRAINING STARTED FOR RUN: {run_id}")
    print("-" * 50)

    for train_file in train_files:
        fold_id = train_file.split("_")[1].split(".")[0]
        train_full_path = os.path.join(f_dir, train_file)

        # 1. Train Algorithm 01 (Naive Baseline)
        # This is the path where we will save the model
        a01_path = os.path.join(m_dir, f"algo01_f{fold_id}.pkl")

        # We will need training duration for Ledger
        start_time = time.time()
        model_trainer.train_algo_01(train_full_path, a01_path)
        duration01 = time.time() - start_time # time in seconds
        train_metrics[f"a01_{fold_id}"] = duration01
        # We store the duration in the dictionary defined before.

        # 2. Train Algorithm 02 (Machine Learning - Decision Tree)
        a02_path = os.path.join(m_dir, f"algo02_f{fold_id}.pkl")
        start_time = time.time()
        model_trainer.train_algo_02(train_full_path, a02_path)
        duration02 = time.time() - start_time  # time in seconds
        train_metrics[f"a02_{fold_id}"] = duration02

        print(f"[STATUS] Fold {fold_id}: Artifacts serialized successfully.")

    # --- PHASE 3: EXECUTION - EVALUATION (The Scientific Audit) ---
    print(f"\n[PHASE 3] PERFORMANCE EVALUATION & LEDGER RECORDING")
    print("-" * 50)

    for train_file in train_files:
        fold_id = train_file.split("_")[1].split(".")[0]
        test_file = f"test_{fold_id}.csv"
        test_full_path = os.path.join(f_dir, test_file)

        # (Timestamp)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 1. Audit Algorithm 01
        m01_path = os.path.join(m_dir, f"algo01_f{fold_id}.pkl")
        acc01, tp01, fp01, tn01, fn01, prec01, rec01, f101 = model_tester.test_model(test_full_path, m01_path, "ALGO01")
        dur01 = train_metrics[f"a01_{fold_id}"]
        model_tester.add_ledger_entry(l_file, ts, run_id, fold_id, "ALGO01", "Naive",
                                      acc01, tp01, fp01, tn01, fn01, prec01, rec01, f101, dur01, MY_SEED)

        # 2. Audit Algorithm 02
        m02_path = os.path.join(m_dir, f"algo02_f{fold_id}.pkl")
        acc02, tp02, fp02, tn02, fn02, prec02, rec02, f102 = model_tester.test_model(test_full_path, m02_path, "ALGO02")
        dur02 = train_metrics[f"a02_{fold_id}"]
        model_tester.add_ledger_entry(l_file, ts, run_id, fold_id, "ALGO02", "Decision_Tree",
                                      acc02, tp02, fp02, tn02, fn02, prec02, rec02, f102, dur02, MY_SEED)

        print(f"[AUDIT] Fold {fold_id} -> Naive: {acc01:.2f} | ML: {acc02:.2f}")

    print("\n" + "=" * 60)
    print(f"EXPERIMENT {run_id} COMPLETED. ALL RECORDS SECURED IN LEDGER.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
