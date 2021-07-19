'''numpy has to be import from settings--> project interpreter --> + --> numpy searching and install'''
import numpy as np

x = np.array([2, 4, 6, 8, 10])   # define a vector

print("type of x is:",type(x))

print("shape of x is:",x.shape)

print(x[0], x[1], x[4])
x[0] = 5
print(x)


# example of defining 2 dimention array

x2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print("print all:\n",x2)
print("type: ", type(x2))
print("shape: ", x2.shape)   # print number of rows and columns
print("data from row0: ",x2[0,0], x2[0,1], x2[0,4])
print("data from row1: ",x2[1,0], x2[1,1], x2[1,4])
print("all row0: ",x2[0])
print("all row1: ",x2[1])

print("Column 0:",x2[:,0]) # print the column
print ("Column 1:",x2[:,1])
x2[0,0] = 500
x2[1,4] = 100
print("all new array:\n",x2)

# example of defining 3 dimension array

x3 = np.array([[ [1 , 2 , 3 , 4 ],
[5 , 6 , 7 , 8 ]],
[ [10, 20, 30, 40],
[50, 60, 70, 80]]])
print("print all:\n",x3[0,0])
print("print all:\n",x3)
print("x3.type: ", type(x3))
print("x3.shape: ", x3.shape)
print("x3[0,0,0]: =",x3[0,0,0])
print("x3[1,1,3]:= ",x3[1,1,3])
print("x3[0,0]=: ",x3[0,0])
print("x3[1,1]=: ",x3[1,1])
print("x3[0,:,0]=",x3[0,:,0])
print("x3[0,:,3]=",x3[1,:,3])
x3[0,0,0] = 500
x3[1,1,3]=100
print("print all:\n",x3)

# another example:

x3 = np.array([[ [1 , 2 ],[3 , 4 ] ],
[ [11, 3],[12, 14] ],
[ [21, 1],[22, 24] ] ])
print("\n all:\n",x3)
print("\n all*2: \n",x3*2)
print("\n all+10: \n",x3+10)
print("\n all*2: \n",x3*2)

# examples of defining spacial matrix

a = np.zeros((4,4)) # init 4X4 zeros matrix
print("np.zero:\n",a)
b = np.ones((1,8)) # init 1X8 ones matrix
print("np.ones:\n",b)
c = np.full((2,2), 7) # init 2X2 matrix of value 7
print("np.full:\n",c)
d = np.eye(5) # init 5X5 identity matrix
print("np.eye:\n",d)
e = np.random.uniform(size=[3,5]) # init 5X3 random matrix wit uniform 0 to 1 random variable
print("uniform(size=[3,5]):\n",e)
f = np.random.uniform(-1,1,size=[2,4]) # init 2X4 random matrix wit uniform -1 to 1 random variable
print("uniform(-1,1,size=[2,4]):\n",f)

# cut 1 dimension array

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\nprint all:\n",x)
print("start=1:stop=7:step=no ",x[1:7])
print("start=5:stop=no:step=no ",x[5:])
print("start=no:stop=5:step=no ",x[:5])
print("start=1:stop=7:step=2 ",x[1:7:2])
print("start=no:stop=no:step=-1 ",x[::-1])
print("start=-3:stop=-6:step=-1 ",x[-3:-6:-1])

# cut 2 dimension array

x2 = np.array([ [1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25] ])
print("\nprint all:\n",x2)
print("axis 0:start=1:stop=4:step=no axis 1:start=1:stop=4:step=no\n",x2[1:4,1:4])
print("axis 0:start=2:stop=no:step=no axis 1:start=2:stop=no:step=no\n",x2[2:,2:])
print("axis 0:start=no:stop=no:step=2 axis 1:start=no:stop=no:step=2\n",x2[::2,::2])
print("axis 0:start=no:stop=no:step=-1 axis 1:start=no:stop=no:step=-1\n",x2[::-1,::-1])
print("axis 0:start=-2:stop=no:step=-1 axis 1:start=-2:stop=no:step=-1\n",x2[-2::-1,-2::-1])

# reshape array

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a = np.reshape(x,(5, 2)) # change shape of x to a 5X2 array
print("reshape(x,(5, 2)):\n",a)
b = np.reshape(x,(10, 1) ) # change shape of x to a 10X1 array
print("reshape(x,(10, 1)):\n",b)
c = np.reshape(x,(2, 5)) # change shape of x to a 2X5 array
print("reshape(x,(2, 5)):\n",c)
# example of logic operation
x1 = np.array([1, 2, 3, 4, 5 ]) # the result will be [4,5]
x2 = x1[x1>3]
print("\n x1>3 : \n",x2)

