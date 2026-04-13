import pandas as pd

# --- 1. DATA LOADING & PREPARATION ---
df = pd.read_csv('survey_data.csv')

# Strategic Age Segmentation (As per your instruction)
bins = [0, 18, 25, 65, 120]
labels = ['Teenager', 'Young Adult', 'Adult', 'Elderly']
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=bins, labels=labels)

likert_cols = [f'Q{i}' for i in range(1, 26)]
demographic_cols = ['GENDER', 'EDUCATION', 'AGE_GROUP']

# --- 2. LIKERT QUALITY ENGINE (ROUTINE CHECKS) ---
def run_quality_checks(data, cols):
    print("=== STEP 1: DATA QUALITY & SANITY CHECK ===")

    # A. Cronbach's Alpha
    item_vars = data[cols].var(axis=0).sum()
    total_var = data[cols].sum(axis=1).var()
    k = len(cols)
    alpha = (k / (k - 1)) * (1 - (item_vars / total_var))
    print(f"[RELIABILITY] Cronbach's Alpha: {alpha:.4f} ({'Pass' if alpha > 0.7 else 'Warning'})")

    # B. Straight-lining (Variance Check)
    # Detects respondents who gave nearly identical answers (Operational Noise)
    data['resp_std'] = data[cols].std(axis=1)
    low_var = data[data['resp_std'] < 0.2]
    print(f"[NOISE] Suspicious straight-liners detected: {len(low_var)}")

    # C. Item-Total Correlation
    # Do specific questions deviate from the general survey trend?
    total_score = data[cols].sum(axis=1)
    correlations = data[cols].corrwith(total_score)
    weak_items = correlations[correlations < 0.3]
    if not weak_items.empty:
        print(f"[CORRELATION] Weak questions found: {weak_items.index.tolist()}")
    print("-" * 45 + "\n")


run_quality_checks(df, likert_cols)

# STRATEGIC NOTE:
# A low Alpha value may also occur due to the following reasons:
# - Failure to reverse-code items: Negatively worded items were not recoded before analysis.
# - Irrelevant items (Noise): Inclusion of variables that do not measure the intended construct.
# - Poor scale design: Low item discrimination, where items fail to distinguish between respondents' differing levels of the trait.
# - Data quality issues: Problems such as outliers, missing values, or inconsistent response patterns.
# - Issues in Likert scale usage: Presence of response bias (e.g., acquiescence bias or social desirability bias).
# What to do then?
# - Exploratory Factor Analysis
# - Item-total correlation / Alpha if Item deleted
# - Factor based Alpha