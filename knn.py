import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter

iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))
def knn_predict(X_train, y_train, x_test_instance, k=3):
    distances = []
    for i in range(len(X_train)):
        dist = euclidean_distance(x_test_instance, X_train[i])
        distances.append((dist, y_train[i]))
    distances.sort(key=lambda x: x[0])
    k_nearest_labels = [label for (_, label) in distances[:k]]
    most_common = Counter(k_nearest_labels).most_common(1)
    return most_common[0][0]
correct = []
incorrect = []
for i in range(len(X_test)):
    x_test_instance = X_test[i]
    true_label = y_test[i]
    predicted_label = knn_predict(X_train, y_train, x_test_instance, k=3)
    if predicted_label == true_label:
        correct.append((x_test_instance, true_label, predicted_label))
    else:
        incorrect.append((x_test_instance, true_label, predicted_label))
print("Correct Predictions:")
for x, actual, predicted in correct:
    print(f"Input: {x}, Actual: {target_names[actual]}, Predicted: {target_names[predicted]}")
print("\nIncorrect Predictions:")
for x, actual, predicted in incorrect:
    print(f"Input: {x}, Actual: {target_names[actual]}, Predicted: {target_names[predicted]}")

accuracy = len(correct) / len(X_test)
print(f"\nAccuracy: {accuracy * 100:.2f}%")
