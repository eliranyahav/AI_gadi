from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
'''sea_list = []
land_list = []
for i in range(1,5):
    img = Image.open("c:/pictures/sea" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    sea_list.append(data[:,:,1].sum() / data[:,:,1].size) # calculate the average number of green
    img = Image.open("c:/pictures/land" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    land_list.append(data[:,:,1].sum() / data[:,:,1].size) # calculate the average number of green
print("\nsea_list:\n",sea_list)
print("\nland_list:\n",land_list)'''



sea_colors = []
for i in range(1,5):
    img = Image.open("c:/pictures/sea" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    t= []
    for i in range(3):
        t.append(data[:,:,i].sum() / data[:,:,i].size)
    sea_colors.append(t)
land_colors = list()
for i in range(1,5):
    img = Image.open("c:/pictures/land" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    t= []
    for i in range(3):
        t.append(data[:,:,i].sum() / data[:,:,i].size)
    land_colors.append(t)
sea_array = np.array(sea_colors) #convert the list data type to numpy data type
land_array = np.array(land_colors) #convert the list data type to numpy data type

#red blue
plt.subplot(131)
sea_array1 = sea_array[:,0]
sea_array2 = sea_array[:,2]
land_array1 = land_array[:,0]
land_array2= land_array[:,2]
plt.plot(sea_array1 , sea_array2 , 'bo', land_array1, land_array2, 'r+')
plt.xlabel("green")
plt.ylabel("blue")
plt.title("Sea or Land option 1")
plt.show()



# green blue
plt.subplot(132)
sea_array1 = sea_array[:,1]
sea_array2 = sea_array[:,2]
land_array1 = land_array[:,1]
land_array2= land_array[:,2]
plt.plot(sea_array1 , sea_array2 , 'bo', land_array1, land_array2, 'r+')
plt.xlabel("green")
plt.ylabel("blue")
plt.title("Sea or Land option 3")
plt.show()
#red green
plt.subplot(133)
sea_array1 = sea_array[:,0]
sea_array2 = sea_array[:,1]
land_array1 = land_array[:,0]
land_array2= land_array[:,1]
plt.plot(sea_array1 , sea_array2 , 'bo', land_array1, land_array2, 'r+')
plt.xlabel("red")
plt.ylabel("green")
plt.title("Sea or Land option 2")
plt.show()