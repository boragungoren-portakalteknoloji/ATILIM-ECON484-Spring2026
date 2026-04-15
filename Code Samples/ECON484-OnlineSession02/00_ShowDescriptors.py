import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.mosaicplot import mosaic

# Load the strategically generated dataset
filename = './Raw Data/raw_data.csv'
df = pd.read_csv(filename)

# 1. BASIC DESCRIPTIVE STATISTICS
print("--- Basic Descriptive Statistics ---")
print(df.describe())
print("\n--- Role Distribution ---")
print(df['ROLE'].value_counts(normalize=True) * 100)

# Setting aesthetic parameters for plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# 2. VISUALIZATION: AGE DISTRIBUTION (Checking the 50% < 35 Rule)
plt.figure(figsize=(10, 6))
sns.histplot(df['AGE'], bins=20, kde=True, color='teal')
plt.axvline(35, color='red', linestyle='--', label='35 Year Threshold')
plt.title('Age Distribution: Identifying Demographic Skew')
plt.xlabel('Biological Age')
plt.ylabel('Employee Count')
plt.legend()
plt.show()

# 3. VISUALIZATION: DIGITAL INTENSITY BY ROLE
# This plot will reveal which departments are 'drowning' in DMs vs Emails
df_melted = df.melt(id_vars=['ROLE'], value_vars=['EMAIL_INTENSITY', 'DM_INTENSITY'],
                    var_name='Communication_Type', value_name='Intensity')

plt.figure(figsize=(12, 6))
sns.barplot(data=df_melted, x='ROLE', y='Intensity', hue='Communication_Type', palette='muted')
plt.title('Average Communication Intensity by Departmental Role')
plt.ylabel('Monthly Message/Email Count')
plt.show()

# 4. MOSAIC CHART: ROLE VS SENIORITY
# Helps to understand the organizational structure and identify 'young leaders' (outliers)
plt.figure(figsize=(14, 10))
mosaic(df, ['ROLE', 'SENIORITY'], title='Organizational Composition: Role vs Seniority')
plt.show()

# 5. THE "OLD SOUL" CORRELATION (Experimental)
# Visualizing if digital noise (DM) correlates with being in high-pressure roles
# regardless of biological age.
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='AGE', y='DM_INTENSITY', hue='ROLE', alpha=0.6)
plt.title('The Age vs. DM Intensity Paradox')
plt.xlabel('Biological Age')
plt.ylabel('DM Intensity (Monthly)')
plt.show()

# 6. SUMMARY INSIGHTS
print("\n--- Strategic Observation ---")
avg_dm_eng = df[df['ROLE'] == 'ENGINEERING']['DM_INTENSITY'].mean()
avg_dm_mgmt = df[df['ROLE'] == 'MANAGEMENT']['DM_INTENSITY'].mean()
print(f"Average DM for Engineering: {avg_dm_eng:.2f}")
print(f"Average DM for Management: {avg_dm_mgmt:.2f}")
print("If Engineering DM is significantly higher, your 'Subjective Aging' theory is statistically viable.")