# HW Assignment 2: Unsupervised Learning and the Decision Ledger

## Overview
In this assignment, we shift from simple data manipulation to **Algorithmic Decision-Making**. Unlike supervised learning, where the data provides the "answers," **Clustering** requires the Lead Architect to find patterns in "unlabeled" data. 

Your goal is to practice the "Discipline of Discovery" by performing a rigorous pre-test analysis before committing to a model. You will use two separate ledgers to defend your choice of features (columns) and parameters ($K$-values). In this course, a "perfect" cluster is useless if you cannot defend the strategy used to find it.

---

## Step 0: Repository Management
1. **New Repository:** Create a private GitHub repository named `ECON484-HW2`.
2. **Environment:** Ensure your PyCharm Professional environment is active with `scikit-learn`, `seaborn`, `pandas`, and `matplotlib` installed.
3. **Atomic Commits:** Commit your work at every logical milestone. 
    * **Mandatory Milestone:** You must perform at least one atomic commit immediately after finishing the pre-test phase. This commit should include your `pretest.py`, `pretest-ledger.csv`, all pre-test plots, and an initial version of your `REPORT.md`.

---

## Your Tasks

### 1. The Dataset: Mall Customer Segmentation
* **Source:** [Kaggle - Mall Customer Segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)
* **Research Requirement:** Before writing code, browse the **"Code"** tab on Kaggle for this dataset. Study how others have handled the data, but remember: you are the Lead Architect. You must implement your own logic.
* **Data Dictionary:**
    * `CustomerID`: Unique identifier (Not a feature for clustering).
    * `Gender`: Categorical identifier.
    * `Age`: Numeric value.
    * `Annual Income (k$)`: Annual income in thousands.
    * `Spending Score (1-100)`: Behavior-based score assigned by the mall.

### 2. Pre-Test Analysis (The "Exploration" Phase)
Create a separate Python file (e.g., `pretest.py`) to understand the data's structure before modeling.
* **Correlation Heatmap:** Identify if any columns are moderately or highly correlated. 
    * *Strategic Task:* If you find a correlated pair, you must later run a comparison in your main assignment: one experiment with the pair included, and one with only one of those columns.
* **Pairplots:** Generate **Pairplots** to visually spot potential clusters. Save at least **5 different pairplot visuals**.
* **Distribution Plots:** Draw and save distribution (histogram/KDE) plots for every numeric column to check for skewness or outliers.
* **Pre-Test Ledger:** Maintain `pretest-ledger.csv` with the following minimal column set:
    * `Plot_ID`: (e.g., PRE-001)
    * `Plot_Type`: (e.g., Heatmap, Pairplot, Distplot)
    * `Columns_Involved`: Which features are being visualized?
    * `Visual_Observation`: What did you see? (e.g., "Income and Spending show 5 distinct groups")
    * `Filename`: The saved image name.

### 3. Execution & "Cloned" Experimentation
In your main clustering script:
* **The "Clone & Drop" Logic:** Your code must clone the original DataFrame for every experiment. Use the clone to drop specific columns to see how the cluster quality changes.
* **Scaling:** You must decide if your features need to be scaled (e.g., `StandardScaler`). You must choose a specific "scaler" and justify why you chose it in your report. 
* **Iteration:** Run the K-Means algorithm for $K$ values between **2 and 8**.
* **Unique Seeds:** Always use your **Student ID** as the `random_state`.

### 4. The Main Experiment Ledger (CSV)
Maintain a `ledger.csv` with **at least 20 rows**. Because you are playing with both $K$ values and different column combinations (using the cloning logic), you should easily reach 20 records. Your ledger must include:
* `Experiment_ID`, `K_Value`, `Columns_Used`, `Silhouette_Score`, `Sensible_Cluster_Names`, and `Plot_Filename`.
* **Note on Names:** For `Sensible_Cluster_Names`, use only spaces to separate names (e.g., "YoungHighSpenders MiddleAgeFrugal"). Do not use commas.

---

## Technical Requirements & Deliverables

### 1. Technical Report (`REPORT.md`)
* **Profile Links:** Links to your GitHub and Kaggle profiles.
* **Pre-Test & Plot Purpose:** Discuss your pre-test procedure. For every plot type generated, explain its purpose and whether it was actually useful for this specific dataset.
* **The Theory:** Include a short discussion (max half a page) on **Supervised vs. Unsupervised Learning** and the use of K-Means. Reference your sources properly.
* **The "Clone" Discussion:** Explain the DataFrame cloning process used in your experiments. Discuss the advantages of this approach and any potential disadvantages (e.g., memory usage or processing overhead).
* **The Scaler & Correlation:** Explain your choice of scaler. Discuss the results of your comparison experiments regarding correlated columns.
* **Decision Defense:** Which experiment produced the most "business-ready" clusters? Defend this choice using your Ledger data and Silhouette scores.
* **Visual Evidence:** Embed your "best" cluster plot and a screenshot of your PyCharm environment.

### 2. Kaggle Visibility
* Upload your code, `ledger.csv`, and `pretest-ledger.csv` as a public Notebook on Kaggle.

---

## Submission Checklist
1. [ ] **GitHub Repo:** `ECON484-HW2` (Private).
2. [ ] **Pre-Test Artifacts:** `pretest.py`, `pretest-ledger.csv`, and all pre-test plots.
3. [ ] **Main Code:** Commented script with cloning and scaling logic.
4. [ ] **The Ledgers:** `ledger.csv` (20+ rows).
5. [ ] **AI Prompts:** `prompts.md` file.
6. [ ] **Final Report:** `REPORT.md` including theoretical discussion, cloning analysis, and Kaggle link.

---

## Pro-Tips for Success
* **Atomic Commits:** Frequent updates prove your process and act as a backup.
* **Lead Architect Mindset:** The AI can write code, but it cannot decide if a cluster name is "sensible" for a business context. That is your responsibility.
