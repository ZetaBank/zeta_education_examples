# What will be Jack's fate?

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

# Data preprocessing process
print("Data Preprocessing Process:")
print("Step 1: Load the ship train and test datasets.")
print("Step 2: Drop unnecessary columns and handle missing values.")
print("Step 3: One-hot encode categorical variables.")
print("Step 4: Define features (X_train) and target variable (y_train) for training data.\n")

# Train the model using the training data
clf.fit(X_train, y_train)

# Data preprocessing for test data
# Drop unnecessary columns and handle missing values
test_data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)
test_data = pd.get_dummies(test_data, columns=['Sex', 'Embarked'], drop_first=True)

# Model training process
print("Model Training Process:")
print("Step 5: Create a Random Forest classifier.")
print("Step 6: Train the model on the preprocessed training data (X_train, y_train).\n")

# Define the characteristics of our fictional character, Jack
jack_features = pd.DataFrame({
    'Pclass': [3],
    'Age': [20],
    'SibSp': [0],
    'Parch': [0],
    'Fare': [7.5],
    'Sex_male': [1],
    'Embarked_Q': [0],
    'Embarked_S': [1]
})

print("Jack's Feature\n", jack_features, "\n")

# Make a prediction for Jack using the trained model
jack_survival_prediction = clf.predict(jack_features)

# Display the initial prediction
if jack_survival_prediction[0] == 1:
    print("Jack would have survived the ship!")
else:
    print("Unfortunately, Jack would not have survived the ship.")