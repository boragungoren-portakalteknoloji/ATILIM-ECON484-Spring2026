import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gower
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

# 1. Load Data
df = pd.read_csv('survey_data.csv')

# Categorize Age (Strategic Segments)
bins = [0, 18, 25, 65, 120]
labels = ['Teenager', 'Young Adult', 'Adult', 'Elderly']
df['AGE_GROUP'] = pd.cut(df['AGE'], bins=bins, labels=labels)

# 2. Features for Mixed-Data Analysis
features = ['GENDER', 'EDUCATION', 'AGE_GROUP'] + [f'Q{i}' for i in range(1, 26)]
cluster_df = df[features].copy()

# CRITICAL FIX: Cast all columns to 'object' dtype to satisfy gower library requirements
# This avoids the StringDtype error in modern Pandas/NumPy
cluster_df = cluster_df.astype(object)

# 3. Compute Gower Distance
print("Computing Gower Distance Matrix (Processing Categorical & Ordinal mix)...")
dist_matrix = gower.gower_matrix(cluster_df)

# 4. Find Optimal Clusters using Silhouette Score
# Silhouette Score validates the cohesion and separation of clusters (Sanity Check)
scores = []
K_range = range(2, 11)

for k in K_range:
    # Agglomerative Clustering is stable for precomputed distance matrices
    model = AgglomerativeClustering(n_clusters=k, metric='precomputed', linkage='average')
    labels = model.fit_predict(dist_matrix)
    score = silhouette_score(dist_matrix, labels, metric='precomputed')
    scores.append(score)

# 5. Visualization
plt.figure(figsize=(10, 6))
plt.plot(K_range, scores, marker='o', linestyle='-', color='darkblue')
plt.title('Validation: Silhouette Score for Cluster Count Optimization')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Coefficient (Higher is Better)')
plt.grid(True, alpha=0.3)
plt.show()

# 6. Comparison of k=2 and k=4 profiles
for k_val in [2, 4]:
    model = AgglomerativeClustering(n_clusters=k_val, metric='precomputed', linkage='average')
    df[f'Cluster_{k_val}'] = model.fit_predict(dist_matrix)
    print(f"\n--- Distribution for k={k_val} ---")
    print(df[f'Cluster_{k_val}'].value_counts())

# Analysis of AGE_GROUP distribution in k=4
# This will show if the higher k value is capturing your age segments better
ct = pd.crosstab(df['AGE_GROUP'], df['Cluster_4'])
print("\nAge Group distribution across 4 clusters:")
print(ct)

# STRATEGIC NOTE:
# The highest point on this graph represents the most 'natural' cluster count
# where respondents are most similar within their groups.

# 7. Dendogram (Again)

from scipy.cluster.hierarchy import dendrogram, linkage

# 7.1. Generate the Linkage Matrix
# We use 'average' linkage to maintain consistency with our AgglomerativeClustering model.
# The distance matrix (Gower) is passed directly to represent the dissimilarities.
linked = linkage(dist_matrix, method='average')

# 7.22. Configure the Dendrogram Plot
plt.figure(figsize=(14, 8))
dendrogram(
    linked,
    orientation='top',
    labels=df['RESP_ID'].values,  # Label leaves with Respondent IDs
    distance_sort='descending',
    show_leaf_counts=True,
    leaf_font_size=10
)

# 7.3. Add Strategic Threshold Lines
# Based on the Silhouette Score, we visualize where the splits for k=2 and k=4 occur.
plt.axhline(y=0.25, color='blue', linestyle='--', label='k=2 Global Split')
plt.axhline(y=0.18, color='red', linestyle='--', label='k=4 Local Sub-clusters')

plt.title('Strategic Hierarchy: Dendrogram Analysis of Survey Respondents', fontsize=15)
plt.ylabel('Gower Dissimilarity Distance')
plt.xlabel('Respondent Identification (RESP_ID)')
plt.legend()

# OPERATIONAL NOTE:
# The vertical height of the lines represents the 'distance' between clusters.
# Large vertical gaps indicate robust, well-separated groupings.
plt.show()

# 8. PCA with Convex Hull Clouds
from sklearn.decomposition import PCA
from scipy.spatial import ConvexHull

# 8.1. Dimensionality Reduction (PCA)
# We project the high-dimensional Gower matrix into 2D space for visualization.
pca = PCA(n_components=2)
coords = pca.fit_transform(dist_matrix)
df['pca_x'] = coords[:, 0]
df['pca_y'] = coords[:, 1]

# 8.2. Visualize Cluster Clouds (Convex Hulls)
plt.figure(figsize=(12, 8))
cluster_colors = ['#4B0082', '#008080', '#FF8C00', '#2E8B57']  # Indigo, Teal, DarkOrange, SeaGreen

for i in range(4):
    # Filter data belonging to the specific cluster
    cluster_subset = df[df['Cluster_4'] == i]

    # Scatter plot for individual respondents
    plt.scatter(
        cluster_subset['pca_x'],
        cluster_subset['pca_y'],
        c=cluster_colors[i],
        label=f'Segment {i}',
        edgecolors='white',
        linewidths=0.5,
        s=80,
        alpha=0.8
    )

    # Generate Convex Hull 'Clouds' to visualize cluster boundaries
    # We need at least 3 points to form a polygon
    if len(cluster_subset) >= 3:
        points = cluster_subset[['pca_x', 'pca_y']].values
        hull = ConvexHull(points)

        # Plotting the hull perimeter
        for simplex in hull.simplices:
            plt.plot(points[simplex, 0], points[simplex, 1], color=cluster_colors[i], lw=2, alpha=0.5)

        # Filling the hull area for a 'cloud' effect
        plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], color=cluster_colors[i], alpha=0.1)

# 8.3. Final Formatting
plt.title('Operational Sanity Check: k=4 Cluster Separation with Convex Hulls', fontsize=14)
plt.xlabel('Principal Component 1 (Major Variance)')
plt.ylabel('Principal Component 2 (Secondary Variance)')
plt.legend(title="Respondent Clusters", loc='best')
plt.grid(True, linestyle=':', alpha=0.6)

# TECHNICAL ASPECT:
# If the hulls (clouds) overlap significantly, it suggests high categorical
# similarity across segments, justifying why k=2 might be mathematically stronger.
plt.show()

# 9. Analyze age
#plt.tight_layout()
#plt.show()

from scipy.stats import chi2_contingency
import seaborn as sns

# 9.1. Contingency Table Construction
# We create a cross-tabulation between our strategic AGE_GROUP and the discovered clusters.
# This table is the foundation for the Chi-Square test.
# Categorize Age (Strategic Segments)
contingency_table = pd.crosstab(df['AGE_GROUP'], df['Cluster_4'])

print("\n--- Operational Sanity Check: Contingency Table (Age vs Cluster) ---")
print(contingency_table)

# 9.2. Chi-Square Test of Independence
# Null Hypothesis (H0): Age Group and Clusters are independent (No relationship).
# Alternative Hypothesis (H1): There is a significant dependency between Age and Clusters.
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f"\nChi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p:.4e}") # Using scientific notation for precision

# 9.3. Statistical Interpretation
# A p-value < 0.05 typically indicates that the clustering is NOT random
# regarding the age segments you defined.
if p < 0.05:
    result_text = "STATISTICALLY SIGNIFICANT: The clusters are heavily influenced by Age Groups."
else:
    result_text = "NOT SIGNIFICANT: Clusters are formed independent of Age Groups (Likert patterns dominate)."

print(f"\nFinal Assessment: {result_text}")

# 9.4. Heatmap Visualization of the Relationship
# Visualizing the density helps identify which specific Age Group 'defines' which cluster.
plt.figure(figsize=(10, 6))
sns.heatmap(contingency_table, annot=True, cmap="YlGnBu", fmt='d', cbar=False)
plt.title(f'Cluster-Age Dependency Heatmap\n(p-value: {p:.4e})', fontsize=12)
plt.ylabel('Strategic Age Segments')
plt.xlabel('Discovered Clusters (k=4)')

# STRATEGIC NOTE:
# If p < 0.05, you have successfully 'captured' the operational reality
# of different age-based behaviors through unsupervised learning.
plt.show()