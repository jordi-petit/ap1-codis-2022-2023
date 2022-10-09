import yogi
import turtle

n = yogi.read(int)
m = yogi.read(int)
aux = 0

for i in range(n*2):
    if i % 2 == 0:
        aux += m
    turtle.forward(aux)
    turtle.left(90)
    

turtle.done()
