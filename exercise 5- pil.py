from PIL import Image
img = Image.open("c:/pictures/bitcoin.jpg")
width, height = img.size
'''img45 = img.rotate(45)
area = (width/2-200, height/2-200, width/2+200, height/2+200)
img_crop = img.crop(area)
newsize = (width//4, height//4)
img_resize = img.resize(newsize)
img_transpose = img.transpose(Image.FLIP_LEFT_RIGHT)
img45.save("c:/pictures/bitcoin45.jpg")
img_crop.save("c:/pictures/bitcoin_crop.jpg")
img_resize.save("c:/pictures/bitcoin_resize.jpg")
print("Old image size:", img.size)
print("New image size:", img_resize.size)
img45.show()
img_crop.show()
img_resize.show()
img_transpose.show()

img = Image.open("c:/pictures/bitcoin.jpg")
img1 = img.convert("L")
img2 = img.convert("1")
img1.show()
img2.show()'''


'''
data = img.getdata()
R = []
G = []
B = []
bw=[]
for i in data:
    R.append((i[0], 0, 0))
    G.append((0, i[1], 0))
    B.append((0, 0, i[2]))
    if ((i[0]+i[1]+i[2])/3 > 70):
        w=255
    else:
        w=0
    bw.append((w,w,w))
imgR = Image.new(mode = "RGB", size = (width, height))
imgG = Image.new(mode = "RGB", size = (width, height))
imgB = Image.new(mode = "RGB", size = (width, height))
imgBW = Image.new(mode = "RGB", size = (width, height))
imgR.putdata(R)
imgG.putdata(G)
imgB.putdata(B)
imgBW.putdata(bw)
for i in range (100):
    print(data[i])
imgR.show()
imgG.show()
imgB.show()
imgBW.show()'''

area = (100, 600, 100, 600)
img_crop = img.crop(area)
data = img_crop.getdata()

imgBIN = Image.new(mode = "RGB", size = (width, height))
imgBIN.putdata(data)

imgBIN.show()