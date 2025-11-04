import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load Titanic dataset
titanic = sns.load_dataset("titanic")
print(titanic.head())
print("Missing values per column:\n", titanic.isnull().sum())
titanic.drop(columns=['deck'], inplace=True)

scaler = StandardScaler()
titanic[['age', 'fare']] = scaler.fit_transform(titanic[['age', 'fare']])
