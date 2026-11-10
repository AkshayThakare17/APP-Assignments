import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

data = {
    'Age': [24, 27, 22, 32, 29, 25, 100, 30, 35, 28],
    'Salary': [50000, 60000, 52000, 58000, 62000, 55000, 600000, 65000, 70000, 58000],
    'Churn': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print("First Five Records:")
print(df.head())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nMean:", df['Age'].mean())
print("Median:", df['Age'].median())
print("Mode:", df['Age'].mode()[0])
print("Standard Deviation:", df['Age'].std())
print("Variance:", df['Age'].var())
print("Minimum:", df['Age'].min())
print("Maximum:", df['Age'].max())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))

plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

sns.boxplot(y=df['Age'])
plt.title("Age Box Plot")
plt.show()

plt.scatter(df['Age'], df['Salary'])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

df['Age_Zscore'] = zscore(df['Age'])
df['Salary_Zscore'] = zscore(df['Salary'])

print("\nOutliers:")
print(df[(df['Age_Zscore'].abs() > 2) | (df['Salary_Zscore'].abs() > 2)])

df['Age'] = df['Age'].clip(
    upper=df['Age'].mean() + 3 * df['Age'].std()
)
df['Salary'] = df['Salary'].clip(
    upper=df['Salary'].mean() + 3 * df['Salary'].std()
)

df.to_csv("cleaned_customer_data.csv", index=False)

print("\nFinal Cleaned Dataset:")
print(df)
