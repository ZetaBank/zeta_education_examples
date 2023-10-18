# Let's change Jack's fate!

# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# File paths
train_file_path = "ship_train.csv"
test_file_path = "ship_test.csv"

# Load the ship train dataset
train_data = pd.read_csv(train_file_path)

# Load the ship test dataset
test_data = pd.read_csv(test_file_path)

# Data preprocessing for training data
# Drop unnecessary columns and handle missing values
train_data.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1, inplace=True)
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
train_data['Fare'].fillna(train_data['Fare'].median(), inplace=True)
train_data = pd.get_dummies(train_data, columns=['Sex', 'Embarked'], drop_first=True)

# Define features and target variable for training data
X_train = train_data.drop('Survived', axis=1)
y_train = train_data['Survived']

# Create a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model using the training data
clf.fit(X_train, y_train)

# Data preprocessing for test data
# Drop unnecessary columns and handle missing values
test_data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)
test_data = pd.get_dummies(test_data, columns=['Sex', 'Embarked'], drop_first=True)

# Explanations for input features
print("\nExplanations for Input Features and Input Ranges:")
print("'Pclass' represents the passenger class (1, 2, or 3).")
print("'Age' represents the age of the passenger (0-100).")
print("'SibSp' represents the number of siblings/spouses aboard (0-8).")
print("'Parch' represents the number of parents/children aboard (0-6).")
print("'Fare' represents the fare paid for the ticket (0-512).")
print("'Sex_male' represents the gender of the passenger (0 for female, 1 for male).")
print("'Embarked_Q' represents whether the passenger embarked at Queenstown (Q) or not (0 or 1).")
print("'Embarked_S' represents whether the passenger embarked at Southampton (S) or not (0 or 1).\n")

# Define the characteristics of our fictional character, Jack
print("Please enter the characteristics of Jack for prediction:")
jack_features = pd.DataFrame({
    'Pclass': [int(input("Pclass: "))],
    'Age': [int(input("Age: "))],
    'SibSp': [int(input("SibSp: "))],
    'Parch': [int(input("Parch: "))],
    'Fare': [float(input("Fare: "))],
    'Sex_male': [int(input("Sex: "))],
    'Embarked_Q': [int(input("Embarked_Q: "))],
    'Embarked_S': [int(input("Embarked_S: "))]
})

# Make a prediction for Jack using the trained model
jack_survival_prediction = clf.predict(jack_features)

# Display the prediction
if jack_survival_prediction[0] == 1:
    print("Jack would have survived the ship!")
else:
    print("Unfortunately, Jack would not have survived the ship.")
