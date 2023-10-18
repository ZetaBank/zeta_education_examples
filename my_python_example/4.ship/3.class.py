# Survival probability estimation chart by seating class

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# File paths
train_file_path = "ship_train.csv"
test_file_path = "ship_test.csv"

# Load the ship train dataset
train_data = pd.read_csv(train_file_path)

# Data preprocessing for the training data
# Drop unnecessary columns and handle missing values
train_data.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1, inplace=True)
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
train_data = pd.get_dummies(train_data, columns=['Sex', 'Embarked'], drop_first=True)

# Calculate survival rates by class
survival_rates = train_data.groupby('Pclass')['Survived'].mean()

# Create a bar chart to visualize survival rates
plt.bar(survival_rates.index, survival_rates.values, color=['lightcoral', 'lightskyblue', 'lightgreen'])
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.title('Survival Rates by Passenger Class')
plt.xticks(survival_rates.index, labels=['1st Class', '2nd Class', '3rd Class'])
plt.ylim(0, 1)
plt.show()