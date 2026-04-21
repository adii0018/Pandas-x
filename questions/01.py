'''1. 🧹 Data Cleaning & Preprocessing (Titanic dataset example)'''
import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

# Drop useless columns
df = df.drop(['PassengerId','Name','Ticket','Cabin'], axis=1)

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Encode categorical variables
df = pd.get_dummies(df, columns=['Sex','Embarked'], drop_first=True)

print(df.head())