import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# Create a new feature: Fare per Person (approx)
titanic['fare_per_person'] = titanic['fare'] / (titanic['alone'].apply(lambda x: 1 if x else 2))
sns.boxplot(x='class', y='fare_per_person', hue='survived', data=titanic)
plt.title("Fare per Person by Class and Survival")
sns.pairplot(titanic[['age','fare','survived','pclass']], hue='survived', palette='coolwarm')
plt.suptitle("Pairplot - Multivariate Relationships", y=1.02)
plt.show()
