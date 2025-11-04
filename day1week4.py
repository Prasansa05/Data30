import seaborn as sns
import matplotlib .pyplot as plt
import pandas as pd

titanic = sns.load_dataset("titanic")
print(titanic.head())
print("Shape of dataset:", titanic.shape)
print("\nColumn names:")
print(titanic.columns.tolist())

print("\nData Info:")
titanic.info()
