import seaborn as sns
from matplotlib import pyplot as plt
tips=sns.load_dataset("tips")
sns.boxplot(x="day",y="total_bill",data=tips)
plt.title("Distribution by days")
plt.show()
