import numpy as np
import matplotlib.pyplot as plt
# Preparing the data for machine learned
dataset = np.loadtxt("c:\data\data1.csv", delimiter=',') # there is problem reading the file.
x = dataset[:0]
y = dataset[:1]
#x=np.array([0,2,3,4,5])
#y=np.array([0,1,2,3,4])
#Learning
def LinearRegression(x,y):
    avgx = np.mean(x)
    avgy = np.mean(y)
    m= (np.sum((x-avgx)*(y-avgy)))/(np.sum((x-avgx)*(x-avgx)))
    b = avgy - m*avgx
    return m,b

m,b =LinearRegression(x,y)
#Generate the graph
y_line = m*x + b
plt.plot(x, y_line, color = "b")
plt.scatter(x, y, color = "g", marker = "o", s = 20)
plt.title('Teen Birth Rate and Poverty Level Data')
plt.xlabel('Poverty Rate')
plt.ylabel('Birth Rate for 15 to 17 year old')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.grid()
plt.show()