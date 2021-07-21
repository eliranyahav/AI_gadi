import matplotlib.pyplot as plt
import numpy as np
train_data = np.array( [     #the data
[ 2.0 , 3.0 ],
[ 3.0 , 7.0 ],
[ 4.0 , 4.0 ],
[ 5.0 , 8.0 ],
[ 6.0 , 5.0 ],
[ 7.0 , 9.0 ],
[ 8.0 , 5.0 ],
[ 8.0 , 2.0 ],
[10.0 , 2.0 ] ])

train_lbl = np.array( [    #the label of the data
[ 1 ],
[ 1 ],
[ 1 ],
[ 1 ],
[ 2 ],
[ 2 ],
[ 2 ],
[ 2 ],
[ 2 ] ])
test_data = np.array( [[ 10 , 8 ]])    # the point need to be predicted
def euclidean_distance(p1, p2):        # function the calcultes the distance between two points
    d = 0.0
    for i in range(len(p1[0])):    # p1 is matrix. p2 is array
        a = float(p1[0,i])    # Here i is the number of the point
        b = float(p2[i])      # Here i is one of the component of the point.
        d += np.power((a-b),2)
    d = np.sqrt(d)
    return d

def KNN(train, test, lbl, K):
    distances = []
    for t, l in zip(train,lbl):
        dist = euclidean_distance(test, t)   # calculate distance
        distances.append((t, dist, l[0]))    # save the point, distance
        print(distances, " ", t, l, "\n")
        distances.sort(key=lambda dist: dist[1])  # sort the distances (from nearest to far
        print(distances," ",t,l,"\n")
        NN = []
    for i in range(K):
        NN.append(distances[i]) # save in NN the nearest neighbours according to k
    print ("nn is: ",NN)
    return NN

def predict(train, test, lbl, K):
    neighbors = KNN(train, test, lbl, K) # get the nearest neighbours
    out = [row[-1] for row in neighbors]  # put in "out" the last label of each point
    print ("out : ",out)

    return max(set(out), key=out.count) # count the most found lable of the neighbours
prediction = predict(train_data, test_data, train_lbl, 3)
print("prediction: " , prediction)
colormap=np.array(['r','g','b'])
color=np.array([1,1,1,1,2,2,2,2,2])

plt.scatter(train_data[:,0],train_data[:,1],c=colormap[color])
plt.scatter(test_data[:,0],test_data[:,1],c='black')
circle2 = plt.Circle((5, 5), 0.5, color='b', fill=False)
plt.show()