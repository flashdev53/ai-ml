import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset from sklearn
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Save it to a CSV file
df.to_csv('iris_dataset.csv', index=False)
