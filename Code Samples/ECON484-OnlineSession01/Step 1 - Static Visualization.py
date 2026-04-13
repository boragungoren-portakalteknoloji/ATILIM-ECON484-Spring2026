import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
import seaborn as sns

# 1. Load the dataset
# Ensure survey_data.csv is in the same directory
df = pd.read_csv('survey_data.csv')

# Apply Seaborn aesthetic theme for professional visualization
sns.set_theme(style="whitegrid")

# 2. Mosaic Plot Configuration
# Scenario: Investigating the relationship between EDUCATION (Categorical Input)
# and Q1 (Categorical/Likert Output) to perform a Sanity Check.

plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["font.size"] = 10

# Helper function to clean internal labels (keeps the plot uncluttered)
label_root = lambda x: ""

# Define properties to highlight specific categories
# This helps in identifying the weight of the 'University' group versus others
props = lambda key: {'color': 'teal' if 'University' in key else 'silver', 'alpha': 0.8}

fig, ax = plt.subplots()

# Generate the Mosaic Plot
# 'gap' parameter adds slight spacing between tiles for better readability
mosaic_obj = mosaic(df, ['EDUCATION', 'Q1'],
                   title='Operational Sanity Check: Education Level vs. Q1 Response Distribution',
                   ax=ax,
                   gap=0.02,
                   labelizer=label_root)

# 3. Final Formatting
plt.xlabel('Education Level (Demographic Input)')
plt.ylabel('Q1 Responses (Likert Scale)')

# STRATEGIC NOTE:
# In the context of the 'Translation Tax' mentioned in your slides,
# visualization is the first step of validation. If 'High School' shows zero
# variance in responses, it indicates a potential bias or data collection error.

