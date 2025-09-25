import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
data = pd.read_csv('iris_data.csv')  # Replace with your CSV file path

# Step 2: Preprocessing (Standardize the data)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Step 3: Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Assume 3 clusters
kmeans_labels = kmeans.fit_predict(scaled_data)

# Step 4: Apply EM (Gaussian Mixture Model)
em = GaussianMixture(n_components=3, random_state=42)  # Assume 3 clusters
em_labels = em.fit_predict(scaled_data)

# Step 5: Evaluate clustering quality using silhouette score
kmeans_silhouette = silhouette_score(scaled_data, kmeans_labels)
em_silhouette = silhouette_score(scaled_data, em_labels)

# Step 6: Print silhouette scores and compare results
print(f"Silhouette Score for K-means: {kmeans_silhouette:.2f}")
print(f"Silhouette Score for EM (Gaussian Mixture): {em_silhouette:.2f}")