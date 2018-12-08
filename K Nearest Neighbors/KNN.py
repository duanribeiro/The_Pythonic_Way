import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix

# Read the data.
df = pd.read_csv('KNN_Project_Data')

# Standardize the variables.
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))

# Train test split division.
X_train, X_test, y_train, y_test = train_test_split(scaled_features, df['TARGET CLASS'], test_size=0.30)

# Creating the model KNN
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)

# Predictions and evaluations
pred = knn.predict(X_test)
matrix = confusion_matrix(y_test, pred)
report =  classification_report(y_test, pred)
print(matrix)
print(report)

# Create a for loop that trains several KNN models with different k-values,
# and then keep a record of the error_rate for each of these models with a list.

error_rate = []
for i in range(1, 10):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10, 6))
plt.plot(error_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('Value of K')
plt.ylabel('Error Rate')
plt.show()