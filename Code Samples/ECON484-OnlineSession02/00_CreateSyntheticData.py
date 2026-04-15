import pandas as pd
import numpy as np

def generate_strategic_test_data(n=1000):
    """
    Generates a 1000-row dataset for testing 'Digital Exhaustion' and 'Subjective Age' perception.
    Incorporates specific demographic distributions and communication patterns with
    intentional outliers to simulate real-world corporate complexity.
    """

    # 1. DEMOGRAPHIC SKEW: 50% under age 35 to simulate a young, tech-heavy workforce.
    # We use two distinct ranges to ensure the 50/50 split requested.
    ages = np.concatenate([
        np.random.randint(25, 36, size=500),
        np.random.randint(36, 66, size=500)
    ])
    np.random.shuffle(ages)

    # 2. DEPARTMENTAL RATIOS: 60% Engineering, 3% Management, 37% shared across Sales, Marketing, Support.
    # This distribution reflects a production-heavy organizational structure.
    roles_list = (['ENGINEERING'] * 600 +
                  ['MANAGEMENT'] * 30 +
                  ['SALES'] * 123 +
                  ['MARKETING'] * 123 +
                  ['SUPPORT'] * 124)
    np.random.shuffle(roles_list)

    df = pd.DataFrame({'AGE': ages, 'ROLE': roles_list})
    df['PERSON_ID'] = range(1, n + 1)

    # 3. SENIORITY MAPPING: Logically linked to age but includes 'High-Potential' outliers.
    def assign_seniority(row):
        # STRATEGIC OUTLIER: High-performing young leaders (Under 30 in Management)
        if row['ROLE'] == 'MANAGEMENT' and row['AGE'] < 30:
            return 'MANAGEMENT'

        # General heuristic for seniority based on biological age
        if row['AGE'] < 30:
            return np.random.choice(['JUNIOR', 'MID'], p=[0.8, 0.2])
        if row['AGE'] < 45:
            return np.random.choice(['MID', 'SENIOR', 'MANAGEMENT'], p=[0.3, 0.6, 0.1])

        # Experienced staff primarily occupy Senior or Management slots
        return np.random.choice(['SENIOR', 'MANAGEMENT'], p=[0.7, 0.3])

    df['SENIORITY'] = df.apply(assign_seniority, axis=1)

    # 4. INTENSITY MODELLING: Simulating digital noise vs. corporate communication.
    # We use Poisson distribution to model frequency (arrival rates) of messages/emails.
    def calculate_intensities(row):
        # Baseline noise levels
        email = np.random.poisson(150)
        dm = np.random.poisson(600)

        # SECTORAL BIAS: Engineering and Support are flooded with Instant Messages (DM).
        if row['ROLE'] == 'ENGINEERING':
            dm += np.random.randint(400, 1000)
            email -= 50
        elif row['ROLE'] == 'MANAGEMENT':
            # Management is often 'trapped' in email threads with high stakeholder overhead.
            email += np.random.randint(500, 1000)
            dm -= 300
        elif row['ROLE'] == 'SUPPORT':
            # Support reflects maximum operational 'noise' and high interruption frequency.
            dm += np.random.randint(1000, 2000)

            # DIGITAL SAVVY OUTLIER: The 'Cool Senior'
        # A small percentage (5%) of older employees who out-message the younger generation.
        if row['AGE'] > 55 and np.random.rand() < 0.05:
            dm += 1500

        return pd.Series([max(0, email), max(0, dm)])

    df[['EMAIL_INTENSITY', 'DM_INTENSITY']] = df.apply(calculate_intensities, axis=1)

    # Column ordering for CSV export
    cols = ['PERSON_ID', 'AGE', 'SENIORITY', 'ROLE', 'EMAIL_INTENSITY', 'DM_INTENSITY']
    return df[cols]


# Execution and CSV Output
df_final = generate_strategic_test_data(1000)
df_final.to_csv('./Raw Data/raw_data.csv', index=False)

# Add Labels and other supervised training related material (ie. dependent variable)
# Load existing data
df = pd.read_csv('./Raw Data/raw_data.csv')

def calculate_perceived_age(row):
    # Start with biological age
    base_age = row['AGE']

    # Impact of Digital Noise (Every 100 DM adds roughly 0.5 year of 'exhaustion')
    dm_impact = row['DM_INTENSITY'] / 200

    # Impact of Corporate Bureaucracy (Every 50 Email adds 1 year of 'perceived age')
    email_impact = row['EMAIL_INTENSITY'] / 50

    # Role-based multipliers (Support and Engineering age faster due to context switching)
    role_stress = {
        'ENGINEERING': 1.2,
        'SUPPORT': 1.5,
        'SALES': 1.1,
        'MARKETING': 1.0,
        'MANAGEMENT': 0.8  # Management is already 'old', impact is lower
    }

    p_age = base_age + (dm_impact + email_impact) * role_stress.get(row['ROLE'], 1.0)

    # Add some 'Human Factor' (Random noise to make it realistic for ML models)
    p_age += np.random.normal(0, 2)
    p_age= round(p_age, 1)

    # --- CATEGORICAL MAPPING ---

    if p_age < 35:
        category = "YOUNG_ADULT"
    elif p_age < 65:
        category = "ADULT"
    else:
        category = "OLD"
    return category

# Apply the logic
df['PERCEIVED_AGE'] = df.apply(calculate_perceived_age, axis=1)

# Save the new version
df.to_csv('./Raw Data/labeled_data.csv', index=False)
print("Updated CSV saved as 'trainingdata-master-v2.csv' with PERCEIVED_AGE column.")

print("SUCCESS: Dataset 'corporate_burnout_study.csv' generated with 1000 records.")
print("DATA PREVIEW:")
print(df_final.head(10))