# HW Assignment 3: The Entropy of Intelligence & Drift Detection

## Overview
A machine learning model is a frozen mathematical snapshot of a specific moment in time. The real world, however, is **non-stationary**. This assignment explores the **"Entropy of Intelligence"**—the inevitable decay of predictive power caused by real-world changes. 

In this lab, you will simulate a "Broken Sensor" network in India. Weather monitoring stations function by converting physical phenomena (voltage, resistance, or light) into digital signals. Statistically, these readings are **events** sampled from a distribution. When a sensor fails or the environment changes, that distribution shifts. 

To experience the "messiness" of real-world data, you will experiment with four specific "Chaos Scenarios":
* **Instance A (The Stuck Sensor):** A mechanical failure where the sensor stops updating. You will replace 20% of `Humidity` or `Temperature` values with a constant (e.g., the mean), simulating a frozen reading.
* **Instance B (Calibration Drift):** A gradual loss of accuracy (e.g., dust on a lens). You will programmatically add a 0.5% incremental multiplier to the `Wind_Speed` feature for every 100 rows.
* **Instance C (The Blackout):** A "Missing Not At Random" (MNAR) pattern. You will simulate a scenario where high pollution levels cause the hardware to fail, resulting in `NaN` (Null) values.
* **Instance D (Concept Drift):** A shift in environmental chemistry. You will artificially shift the target `PM2.5` values by a margin while keeping features the same, simulating a world where the model’s old logic no longer applies.

---

## Step 0: The Lead Architect’s Briefing (`random_forest_explained.md`)
Before touching the data, you must understand your tool: the **Random Forest (RF)**. 
* **Research Task:** Create a 2-3 page Markdown document explaining the RF mechanism (bagging), its response to the four drift types above, and the difficulty of detecting "silent failures" in ensemble models.
* **Requirement:** Formal academic references are mandatory for this research.

---

## Step 1: The Foundation (Baseline & Chaos)

### A. The Dataset: Air Quality in India
For non-engineers, treat these columns as "Atmospheric Vital Signs":
* **PM2.5 / PM10:** Tiny dust/soot particles. 
* **NOx / SO2 / CO:** Toxic gases measured in parts per billion.
* **AQI (Target):** The calculated Air Quality Index—the "Health Score" your model must predict.

### B. The Baseline Model
Find an existing **Kaggle solution** for this dataset and audit their logic:
1.  Train a single Random Forest model using your **Student ID** as the `random_state`.
2.  **Save the Model:** Export your trained model as a file (e.g., `baseline_model.pkl`) using `pickle` or `joblib`.

### C. The Chaos Generator
Create a **separate Python script** (`chaos_generator.py`). This script must load your clean test set and output **four separate "Drifted" CSV files** representing the instances described in the Overview.

---

## Step 2: The Multi-Stage Experiment Ledger (`ledger.csv`)
Maintain a scientific record of **at least 30 rows**, including a "None" type for the baseline.
* **Required Columns:** `Experiment_ID`, `Drift_Type`, `Drift_Parameter` (Severity), `Mean_Shift`, `KS_Test_P_Value`, `Detection_Latency` (how many rows passed before you noticed the shift?), `Baseline_R2`, and `Drifted_R2`.

---

## Step 3: Detection Logic (Pre-Inference)
Implement **Early Warning Systems** using `scipy.stats.ks_2samp` to prove the distribution has changed. You must attempt to detect the drift as early as possible in the data stream to minimize the "Cost of Late Detection."

---

## Step 4: Technical Report (`REPORT.md`)
* **Cloning & Memory:** Discuss the advantages/disadvantages of cloning dataframes and the RAM overhead of managing multiple parallel "drifted" datasets.
* **The Strategic Manager’s Review:** Is **retraining** always the answer? Compare "Algorithm Adjustment" vs. "Cleaning the Physical Equipment."
* **Economic Impact:** Discuss the cost of late detection. If a sensor drifts for weeks before your model catches it, what are the real-world consequences for public health policy?
* **Code Hygiene:** Research **Linters vs. Soft Linters**. Explain your formatting choices for this lab.

---

## Submission Checklist
1. [ ] **Research Doc:** `random_forest_explained.md` (with references).
2. [ ] **Model File:** `baseline_model.pkl`.
3. [ ] **All Code Assets:** Including the training script, `chaos_generator.py`, and detection logic.
4. [ ] **The Ledgers:** `ledger.csv` (30+ rows).
5. [ ] **Final Report:** `REPORT.md` including the Economic Impact discussion and Kaggle link.
