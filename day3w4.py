import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

print(titanic.head())
print(titanic.info())
numeric_cols = titanic.select_dtypes(include=['float64', 'int64']).columns
print("Numeric Columns:", numeric_cols)
print(titanic[numeric_cols].describe())

# Skewness and Kurtosis
print("\nSkewness:\n", titanic[numeric_cols].skew())
print("\nKurtosis:\n", titanic[numeric_cols].kurt())
