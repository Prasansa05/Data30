import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
plt.figure(figsize=(6,4))
sns.scatterplot(x='age', y='fare', data=titanic, hue='survived', palette='cool')
plt.title("Age vs Fare (Colored by Survival)")
plt.show()
corr = titanic.corr(numeric_only=True)
print(corr)
