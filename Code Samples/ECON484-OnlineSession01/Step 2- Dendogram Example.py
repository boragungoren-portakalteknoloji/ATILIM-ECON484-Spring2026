import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. Load data and select Likert questions (Q1-Q25)
df = pd.read_csv('survey_data.csv')
questions_df = df.filter(regex='^Q')

# 2. Transpose data to cluster questions (columns) instead of respondents (rows)
# This allows us to see which questions are linked based on respondent behavior.
data_to_cluster = questions_df.T

# 3. Perform Hierarchical Clustering
# We use 'ward' method to minimize variance within clusters
linked = linkage(data_to_cluster, method='ward')

# 4. Visualization
plt.figure(figsize=(12, 7))
dendrogram(linked,
           labels=questions_df.columns,
           leaf_rotation=90,
           leaf_font_size=10,
           color_threshold=0) # Set threshold to 0 to keep it monochrome or adjust for color clusters

plt.title('Hierarchical Clustering of Survey Questions (Q1-Q25)')
plt.xlabel('Question ID')
plt.ylabel('Distance (Similarity)')

# OPERATIONAL NOTE:
# Look for Q1-Q9, Q3-Q12-Q17 pairs. They should be clustered closely.
# High distance (vertical line height) indicates dissimilarity.
plt.show()