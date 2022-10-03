from yogi import read
import turtle as tl

n=read(int)#costats
m=read(int)#tamany
j=0
tl.setposition(0,0)


for x in range(n): #número de repeticions verticals

    for j in range(n): #número de repeticions en horitzontal
        for i in range(4):#per fer el quadrat
            tl.forward(m)
            tl.left(90)
        tl.forward(m)
    tl.left(90)
    tl.forward(m)
    tl.left(90)
    tl.forward(n*m)
    tl.right(180)

tl.done()
