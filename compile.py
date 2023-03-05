from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
import pandas as pd
import joblib

# Load the dataset
df = pd.read_csv('dataset/constellation_data.csv')

# Split the dataset into training and testing sets
X = df.drop('constellation_name', axis=1)
y = df['constellation_name']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

imputer = SimpleImputer(strategy='constant', fill_value=-5)
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Train the model
k = 5
model_num = 25
model = KNeighborsClassifier(n_neighbors=k)
print(f"Training model v{model_num} with k={k}....")
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Save the model
joblib.dump(model, f'models/model{model_num}.sav')