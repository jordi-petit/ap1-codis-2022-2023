# programa que pinta un poligon de n costats

from turtle import *
from yogi import *

n = read(int)
i = 1
while i <= n:
    forward(30)
    right(360 / n)
    i = i + 1
done()
