import numpy as np
import matplotlib.pyplot as plt
# how to plot graph

x=[1,5]
y=[1,5]
plt.title("y vs x")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,'go')
plt.axis([0,10,0,20])
plt.show()

x=[]
y1=[]
y2=[]
for i in range(0,30):
    x.append(i)
    y1.append(pow(i,2.5)) #pow(x,y) calculates the y power of x
    y2.append(pow(i,3))
plt.plot(x, y1, 'b--')  # b for blue, -- for the shape of the line
plt.plot(x, y2, 'g.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



t= np.arange(0.0, 2.0, 0.01)
s = 3*np.sin(2 * np.pi * t)
plt.axis([0,3,-3,3])
plt.plot(t, s)
plt.grid() # display grid lines
plt.title("Sine wave")
plt.xlabel("time (s)")
plt.ylabel("sine wave")
plt.show()

a= np.array([ [1,2,3,4,5,6,7,8,9,10],
[1,3,7,4,8,5,9,7,3,2] ])
categories = np.array([0,0,0,1,1,1,1,2,2,2])
colormap = np.array(['r', 'g', 'b'])
plt.scatter(a[0], a[1], s=50, c=colormap[categories]) # s - the radius of the dot, colormap gets 0,1,2 correponding to categories and r,g,b
plt.show()