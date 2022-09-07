# programa que pinta 12 poligons de n costats rotats al seu centre

from turtle import *
from yogi import *

n = read(int)

# amb aquestes dues línies la tortuga és més ràpida 🐢🏁!
speed(0)
hideturtle()

j = 1
while j <= 12:      # <------------------- bucle extern
    # inici pintar poligon de n costats
    i = 1
    while i <= n:   # <------------------- bucle intern
        forward(30)
        right(360 / n)
        i = i + 1
    # final pintar poligon de n costats

    j = j + 1
    right(360 / 12)
done()
