import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 1: Load the dataset
# Replace 'your_dataset.csv' with your actual CSV file path
data = pd.read_csv('iris_dataset.csv')

# Step 2: Preprocessing
# Drop any non-numeric columns (if any) or handle missing values
# For simplicity, let's assume we're working with numeric columns only
# If you have missing values, you can use data.fillna() or dropna()

# Optionally scale data (important for distance-based algorithms like K-means)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Step 3: Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Assume 3 clusters as an example
kmeans_labels = kmeans.fit_predict(scaled_data)

# Step 4: Apply EM clustering (Gaussian Mixture Model)
em = GaussianMixture(n_components=3, random_state=42)  # Assume 3 clusters
em_labels = em.fit_predict(scaled_data)

# Step 5: Evaluate clustering quality
# Calculate the silhouette score for K-means
kmeans_silhouette = silhouette_score(scaled_data, kmeans_labels)

# Calculate the silhouette score for EM
em_silhouette = silhouette_score(scaled_data, em_labels)

# Step 6: Visualize the clusters using PCA (for 2D visualization)
# Use PCA to reduce the data to 2D for visualization
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

# Plot K-means clusters
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans_labels, cmap='viridis', s=50)
plt.title(f"K-means Clustering (Silhouette: {kmeans_silhouette:.2f})")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")

# Plot EM clusters
plt.subplot(1, 2, 2)
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=em_labels, cmap='plasma', s=50)
plt.title(f"EM Clustering (Silhouette: {em_silhouette:.2f})")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")

plt.show()

# Step 7: Output the comparison
print(f"Silhouette Score for K-means: {kmeans_silhouette:.2f}")
print(f"Silhouette Score for EM (Gaussian Mixture): {em_silhouette:.2f}")

# Optional: Inertia for K-means
print(f"K-means Inertia: {kmeans.inertia_:.2f}")
