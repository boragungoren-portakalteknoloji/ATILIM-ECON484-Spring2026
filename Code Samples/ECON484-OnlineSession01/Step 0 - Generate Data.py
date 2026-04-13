import pandas as pd
import numpy as np

# Seed for random number generation
np.random.seed(42)

n = 100

# 1. RESP_ID: RESP-ABCD-0001 format
resp_ids = [f"RESP-ABCD-{i:04d}" for i in range(1, n + 1)]

# 2. GENDER Distribution: %5 Unspecified, %45 Male, %50 Female
genders = np.random.choice(
    ['Unspecified', 'Male', 'Female'], 
    size=n, 
    p=[0.05, 0.45, 0.50]
)

# 3. AGE: 20-45  normal Distribution (Average 32, Std Deviance 7)
ages = np.random.normal(loc=32, scale=7, size=n).astype(int)
ages = np.clip(ages, 20, 45) # Sınırları koru

# 4. EDUCATION Distribution: %3 Unspecified, %10 High School, %10 Masters+, %77 University
educations = np.random.choice(
    ['Unspecified', 'High School', 'Masters or above', 'University'],
    size=n,
    p=[0.03, 0.10, 0.10, 0.77]
)

# Constraint: 5 Samples Age: 20-21 Education:University
# Edit 5 random data points
constraint_indices = np.random.choice(range(n), 5, replace=False)
for idx in constraint_indices:
    ages[idx] = np.random.choice([20, 21])
    educations[idx] = 'University'

# 5. Q1-Q25 Likert VeriDAtaleri (1, 3, 5, 7, 9)
likert_options = [1, 3, 5, 7, 9]
q_data = {}

# First fill with random data
for i in range(1, 26):
    q_data[f'Q{i}'] = np.random.choice(likert_options, size=n)

# Constraint: Make consistent with some noise
def make_consistent(base_q, target_q):
    noise = np.random.choice([-2, 0, 2], size=n, p=[0.1, 0.8, 0.1])
    consistent_vals = q_data[base_q] + noise
    q_data[target_q] = np.clip(consistent_vals, 1, 9)
    q_data[target_q] = np.array([min(likert_options, key=lambda x:abs(x-val)) for val in q_data[target_q]])

# Matched consistencies
make_consistent('Q1', 'Q9')
make_consistent('Q3', 'Q12')
make_consistent('Q3', 'Q17')
make_consistent('Q5', 'Q8')
make_consistent('Q11', 'Q22')

# Unify dataframe
df = pd.DataFrame({
    'RESP_ID': resp_ids,
    'GENDER': genders,
    'AGE': ages,
    'EDUCATION': educations
})

# Add questions
df_questions = pd.DataFrame(q_data)
df = pd.concat([df, df_questions], axis=1)

# Save as CSV
df.to_csv('survey_data.csv', index=False)

print("Veri seti 'survey_data.csv' adıyla oluşturuldu.")
print(df.head())