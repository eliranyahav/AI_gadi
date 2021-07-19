class MyDice(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.sum=x+y
    def addx(self,x):
        self.x+=x
    def addy(self,y):
        self.y+=y

m=MyDice(3,4)
print(m.x)
print (m.sum)
m.addx(5)
m.addy(10)
print(m.x)
print(m.y)
