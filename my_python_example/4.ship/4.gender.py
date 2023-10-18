# Probability of death estimation chart by gender

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

# Calculate the probability of death by gender
death_probabilities = 1 - train_data.groupby('Sex_male')['Survived'].mean()

# Create a bar chart to visualize the probability of death by gender
plt.bar(death_probabilities.index, death_probabilities.values, color=['lightcoral', 'lightblue'])
plt.xlabel('Gender')
plt.ylabel('Probability of Death')
plt.title('Probability of Death by Gender')
plt.xticks(death_probabilities.index, labels=['Female', 'Male'])
plt.ylim(0, 1)
plt.show()
