import seaborn as sns
from matplotlib import pyplot as plt
iris=sns.load_dataset('iris')
print(iris.head())
print("\nSummary:")
print(iris.describe())
sns.boxplot(data=iris)
plt.show()
 
