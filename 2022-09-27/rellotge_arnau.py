from turtle import *
from yogi import read
h=read(int)
m=read(int)
up()
goto(0,-200)
down()
def forma():
    for i in range(12):
        circle(200,30)
        lt(90)
        fd(50)
        lt(180)
        fd(50)
        lt(90)
    up()
    lt(90)
    fd(200)
    down()
def minuts():
    rt(6*m)
    fd(140)
    rt(150)
    for i in range(3):
        fd(25)
        rt(120)
    rt(30)
    fd(140)
    seth(90)
def hores():
    rt(30*h + 30*m//60 )
    fd(90)
    rt(150)
    for i in range(3):
        fd(25)
        rt(120)
    rt(30)
    fd(90)
speed(0)
forma()
minuts()
hores()

done()
