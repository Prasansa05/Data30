import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Basic cleaning
titanic.dropna(subset=['age', 'fare', 'sex', 'class', 'survived'], inplace=True)
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('coolwarm')
# Create 2x2 layout for dashboard
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

#Survival Count
sns.countplot(ax=axes[0,0], x='survived', data=titanic, palette='pastel')
axes[0,0].set_title('Overall Survival Count')
axes[0,0].set_xlabel('Survived (1 = Yes, 0 = No)')
axes[0,0].set_ylabel('Passenger Count')

#Survival by Gender
sns.countplot(ax=axes[0,1], x='sex', hue='survived', data=titanic)
axes[0,1].set_title('Survival by Gender')
axes[0,1].set_xlabel('Gender')
axes[0,1].set_ylabel('Count')

#Survival by Class
sns.barplot(ax=axes[1,0], x='class', y='survived', data=titanic, ci=None)
axes[1,0].set_title('Survival Rate by Passenger Class')
axes[1,0].set_xlabel('Class')
axes[1,0].set_ylabel('Survival Probability')

#Age vs Fare (Colored by Class)
sns.scatterplot(ax=axes[1,1], x='age', y='fare', hue='class', data=titanic)
axes[1,1].set_title('Age vs Fare by Class')
axes[1,1].set_xlabel('Age')
axes[1,1].set_ylabel('Fare')

plt.suptitle(' Titanic Dataset Dashboard: Summary of Key Insights', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()
