

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('titanic.csv.txt')

# 1. Explore data structure
print(df.shape)
print(df.info())
print(df.head())
print(df.describe())

# 2. Check for data issues
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# 3. Identify trends and patterns
print(df['Survived'].value_counts())
print(df['Pclass'].value_counts())
print(df.corr(numeric_only=True))

# Heatmap of correlations
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 4. Detect outliers/anomalies
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Age'])
plt.title("Age Distribution (Outlier Check)")
plt.show()

# 5. Test a hypothesis: Did class affect survival?
plt.figure(figsize=(6,4))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title("Survival Rate by Passenger Class")
plt.show()

# Another hypothesis: Did gender affect survival?
plt.figure(figsize=(6,4))
sns.barplot(x='Sex', y='Survived', data=df)
plt.title("Survival Rate by Gender")
plt.show()



import pandas as pd
df = pd.read_csv('titanic.csv.txt')
print(df.shape)
print(df.head())   


































