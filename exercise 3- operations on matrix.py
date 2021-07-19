import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
x = a + b
print("a + b:\n",x)
x=x+2
print("x+2:\n",x)
x=x/2
print("x/2:\n",x)
x=a*b
print("a*b\n:",x)

a = np.array([[1, 2, 1], [0, 1, 0]])
b = np.array([[2, 5], [6, 7], [1, 8]])
c = a.dot(b)
print("a:\n",a)
print("b:\n",b)
print ("a.dot(b):\n",c)

x2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
a = x2.transpose() # calculate the transpose matrix
b = x2.T # same as transpose()
print("x2:\n",x2)
print("x2.transpose():\n",a)
print("x2.T:\n",b)