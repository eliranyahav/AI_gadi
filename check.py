import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,2,3,4,5])
y=np.array([0,1,2,3,4])

avgx=np.mean(x)
avgy=np.mean(y)

m = (np.sum((x-avgx)*(y-avgy)))/(np.sum((x-avgx)*(x-avgx)))
print(m)
b=avgy-m*avgx
print(b)
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