import pandas as pd

data=pd.read_csv('student.csv')
print("Basic info")
print(data.info())
print("-" * 50)
print("top 5 rows")
print(data.head())
print("-" * 50)
print("sumaary statistics")
print(data.describe)
print("-" * 50)
