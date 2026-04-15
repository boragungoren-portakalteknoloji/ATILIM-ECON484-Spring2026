import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def analyze_latest_run(run_path):
    """
    PURPOSE: Automated Performance Auditing (Slide 75).
    Translates raw Ledger data into strategic insights by comparing
    the Naive baseline (Algo 01) against the ML model (Algo 02).
    """

    ledger_path = os.path.join(run_path, "ledger.csv")
    if not os.path.exists(ledger_path):
        print(f"[ERROR] Audit failed: Ledger not found at {ledger_path}")
        return

    # Load and Sanitize Schema
    df = pd.read_csv(ledger_path)
    df.columns = df.columns.str.strip()  # Defensive programming against whitespace

    # 1. STRATEGIC AGGREGATION (Slide 72)
    # Aggregating metrics to assess 'Average Operational Value'.
    # Note: We use 'F1_Score' as the primary KPI to balance Precision and Recall.
    metrics_of_interest = ['Accuracy', 'F1_Score', 'Train_Duration']
    summary = df.groupby('Algorithm')[metrics_of_interest].mean()

    print("\n" + "=" * 50)
    print("STRATEGIC AUDIT SUMMARY: ALGORITHMIC COMPARISON")
    print("=" * 50)
    print(summary)

    # 2. ROI CALCULATION: ML ADVANTAGE
    # Quantifying the 'Value Add' of our Decision Tree model.
    naive_f1 = summary.loc['ALGO01', 'F1_Score']
    ml_f1 = summary.loc['ALGO02', 'F1_Score']
    improvement = (ml_f1 - naive_f1) / naive_f1 * 100

    print(f"\n[INSIGHT] The ML Model provides a {improvement:.2f}% efficiency gain over the Baseline.")

    # 3. VISUALIZATION: STABILITY & VARIANCE (Slide 4)
    # Assessing if the model is robust across different data folds or prone to noise.
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Fold_ID', y='F1_Score', hue='Algorithm', marker='o', linewidth=2.5)
    plt.title('Performance Stability: F1_Score Consistency Across K-Folds', fontsize=14)
    plt.ylabel('F1_Score (Macro Average)')
    plt.xlabel('Fold Identifier (Cross-Validation Step)')
    plt.grid(True, linestyle='--', alpha=0.6)

    # Exporting artifacts for the Lab Notebook (Slide 3)
    plt.savefig(os.path.join(run_path, "performance_stability.png"))

    # 4. VISUALIZATION: ERROR ARCHITECTURE (Algo 02 Audit)
    # Breaking down the Failure Mode: Are we over-predicting (FP) or missing (FN)?
    df_ml = df[df['Algorithm'] == 'ALGO02']
    plt.figure(figsize=(10, 6))

    error_summary = pd.DataFrame({
        'Error Category': ['False Positives (Aggressive)', 'False Negatives (Passive)'],
        'Total Count': [df_ml['FP'].sum(), df_ml['FN'].sum()]
    })

    sns.barplot(data=error_summary, x='Error Category', y='Total Count', palette='viridis')
    plt.title('ML Error Profile: Assessing Systematic Bias', fontsize=14)
    plt.ylabel('Aggregate Error Count (Total Samples)')

    plt.savefig(os.path.join(run_path, "error_profile.png"))
    print(f"\n[VISUAL] Audit Visuals exported successfully to: {run_path}")
    plt.show()


if __name__ == "__main__":
    # AUTOMATION: Detecting the most recent experiment for analysis
    exp_dir = "Experiments"
    if os.path.exists(exp_dir):
        latest_run = sorted([d for d in os.listdir(exp_dir) if d.startswith("run_")])[-1]
        analyze_latest_run(os.path.join(exp_dir, latest_run))
    else:
        print("[CRITICAL] No 'Experiments' directory found. Run 03_RunExperiment.py first.")


# Summary: The Feature-Reality Gap Analysis
#
# The current experiment results reveal a critical Strategic Red Flag: our Machine Learning model (Algo 02)
# is consistently underperforming compared to the Naive Heuristic (Algo 01). This phenomenon, known as
# "Negative Value Add," occurs when a complex system fails to outperform a simple rule.

# 1. The Dominance of Biological Anchors
# The Naive model’s superior performance proves that Chronological Age remains the most powerful predictor
# of "Perceived Age." Human perception is deeply anchored in biological reality. Simple heuristic rules
# (e.g., "If Age > 40, then Person is Old") provide a high-integrity baseline that is difficult to disrupt
# without high-quality digital signals.

# 2. The Digital Signal-to-Noise Problem
# The core failure lies in the Digital Features (DM counts, Email frequency, etc.). These metrics are currently
# acting as "Digital Noise" rather than "Digital Intelligence":
#  - Weak Proxy: High email frequency does not inherently signal "Adult" or "Professional" status; a student
#    may be as digitally active as a CEO.
#  - Context Vacuum: Our features measure quantity but ignore context. Without "Sentiment" or "Engagement Quality,"
#     we are feeding the model "Digital Exhaust" that confuses the Decision Tree rather than clarifying it.
#   - Feature Dilution: When the ML model attempts to find patterns in these weak digital signals, it effectively
#     ignores the strong "Age" signal, leading to the performance drop observed in the stability charts.

# 3. Decision Defense
# To rescue the project from its current state of Underfitting, we may pivot from "Quantitative Features" to
# "Qualitative Insights":
# - Behavioral Clustering: Instead of raw counts, we may try to measure "Digital Rhythms"
#   (e.g., late-night activity vs. business-hour activity).
# - Aggressive Feature Selection: We can prune the digital features that show zero correlation with the
#   target and focus only on those that complement the biological age.
# - The Baseline Rule: If a feature does not increase the F1-Score of the Naive baseline, it must be
#   discarded to maintain Operational Resilience.

# 4. Final Verdict
# In its current form, complexity is our enemy. We have built a "Technological Overhead" that delivers
# less value than a simple logic gate. We must either find High-Fidelity Features that capture the "essence" of
# perceived age or accept that digital footprints, in their current sallow form, cannot override
# biological reality.