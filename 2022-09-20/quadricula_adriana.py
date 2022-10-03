from yogi import read
import turtle

n=read(int)
m=read(int)
c=1
i=1


while c<=n+1 and i<3:

    if c%2==1 and c<=n:
        turtle.forward(m*n)
        turtle.left(90)
        turtle.forward(m)
        turtle.left(90)
        c=c+1   
    elif c%2==0 and c<=n:
        turtle.forward(m*n)
        turtle.right(90)
        turtle.forward(m)        
        turtle.right(90)
        c=c+1
    elif c==n+1:
        turtle.forward(m*n)
        if n%2==1:
            turtle.left(90)
            c=1
            i=i+1
        else:
            turtle.right(180) 
            turtle.forward(m*n)
            turtle.left(90)
            c=1
            i=i+1
turtle.done()
