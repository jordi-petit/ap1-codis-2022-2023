import re
from yogi import read
import turtle

s = read(str)
n = read(int)

if s == "quadrat":
    for i in range (4):
        turtle.forward(n)
        turtle.left(90)
elif s == "cercle": 
    turtle.circle(n)
else:
    m = read(int)
    for i in range (2):
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(m)
        turtle.left(90)

turtle.done()