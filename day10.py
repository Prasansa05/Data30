from matplotlib import pyplot as plt
x=[250,350,450,500,650]
y=[1,2,3,4,5]
plt.plot(x,y,linewidth=5)
plt.title('Sales over months')
plt.xlabel('Sales')
plt.ylabel('Months')
plt.grid(True,color='k')
plt.show()
