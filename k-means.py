import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 1: Load the Wine dataset
wine = load_wine()
data = pd.DataFrame(wine.data, columns=wine.feature_names)
true_labels = wine.target  # True wine class labels (0, 1, 2)

# Step 2: Preprocessing
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Step 3: Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(scaled_data)

# Step 4: Apply EM clustering (Gaussian Mixture Model)
em = GaussianMixture(n_components=3, random_state=42)
em_labels = em.fit_predict(scaled_data)

# Step 5: Evaluate clustering quality
kmeans_silhouette = silhouette_score(scaled_data, kmeans_labels)
em_silhouette = silhouette_score(scaled_data, em_labels)

# Step 5.1: Calculate ARI
kmeans_ari = adjusted_rand_score(true_labels, kmeans_labels)
em_ari = adjusted_rand_score(true_labels, em_labels)

# Step 6: Visualize the clusters using PCA
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans_labels, cmap='viridis', s=50)
plt.title(f"K-means Clustering\nSilhouette: {kmeans_silhouette:.2f}, ARI: {kmeans_ari:.2f}")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")

plt.subplot(1, 2, 2)
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=em_labels, cmap='plasma', s=50)
plt.title(f"EM Clustering\nSilhouette: {em_silhouette:.2f}, ARI: {em_ari:.2f}")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")

plt.show()

# Step 7: Output the comparison
print("🍷 Clustering Evaluation Metrics on Wine Dataset")
print(f"Silhouette Score for K-means: {kmeans_silhouette:.2f}")
print(f"ARI for K-means: {kmeans_ari:.2f}")
print(f"Silhouette Score for EM (Gaussian Mixture): {em_silhouette:.2f}")
print(f"ARI for EM (Gaussian Mixture): {em_ari:.2f}")
print(f"K-means Inertia: {kmeans.inertia_:.2f}")
