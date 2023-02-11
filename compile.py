# Import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the .csv file into a Pandas dataframe
df = pd.read_csv('dataset/constellation_data.csv')

# Replace NaN values with a placeholder
df.fillna(0, inplace=True)

# Split the data into training and testing sets
X = df.iloc[:, 1:]
y = df.iloc[:, 0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train a random forest classifier on the training data
classifier = RandomForestClassifier(n_estimators=200, random_state=0)
classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = classifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# Save the model to a file
filename = 'models/model_new.sav'
joblib.dump(classifier, filename)