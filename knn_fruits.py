import numpy as np
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
data = {
    'Weight': [150, 200, 120, 180, 75, 130, 190],
    'Color': [0, 1, 0, 1, 2, 0, 2],
    'Size': [6, 7, 5, 6.5, 4, 5.5, 6.2],
    'Type': ['Apple', 'Banana', 'Apple', 'Banana', 'Orange', 'Apple', 'Orange']
}
df = pd.DataFrame(data)
X = df[['Weight', 'Color', 'Size']].values
y = df['Type'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(df)
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
    print(f"Input: {x}, Actual: {actual}, Predicted: {predicted}")
print("\nIncorrect Predictions:")
for x, actual, predicted in incorrect:
    print(f"Input: {x}, Actual: {actual}, Predicted: {predicted}")
accuracy = len(correct) / len(X_test)
print(f"\nAccuracy: {accuracy *100:.2f}%")