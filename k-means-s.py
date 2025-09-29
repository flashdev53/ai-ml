import pandas as pd
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.preprocessing import StandardScaler

# Step 1: Load the Wine dataset
wine = load_wine()
data = pd.DataFrame(wine.data, columns=wine.feature_names)
true_labels = wine.target  # True wine class labels (0, 1, 2)

# Step 2: Preprocessing (Standardize the features)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Step 3: Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(scaled_data)

# Step 4: Apply EM (Gaussian Mixture Model)
em = GaussianMixture(n_components=3, random_state=42)
em_labels = em.fit_predict(scaled_data)

# Step 5: Evaluate clustering quality
kmeans_silhouette = silhouette_score(scaled_data, kmeans_labels)
em_silhouette = silhouette_score(scaled_data, em_labels)

kmeans_ari = adjusted_rand_score(true_labels, kmeans_labels)
em_ari = adjusted_rand_score(true_labels, em_labels)

# Step 6: Print results
print("🍷 Clustering Evaluation Metrics on Wine Dataset")
print(f"K-means Silhouette Score: {kmeans_silhouette:.2f}")
print(f"EM Silhouette Score: {em_silhouette:.2f}")
print(f"K-means ARI: {kmeans_ari:.2f}")
print(f"EM ARI: {em_ari:.2f}")
