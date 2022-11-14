import turtle
import cmath
import math
import colorsys

#Get gutter

def setwindowsize(x=640, y=640):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0,0,x,y)

def showimage():
    turtle.hideturtle()
    turtle.update()

def drawpixel(x, y, color, pixelsize = 1 ):
    turtle.tracer(0, 0)
    turtle.colormode(1.0)
    turtle.penup()
    turtle.setpos(x*pixelsize,y*pixelsize)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(pixelsize)   
    turtle.end_fill()


def JuliaPoly():
    print("Power of Julia Polynomial:")
    p = 2
    print("Complex Contast c (need two numbers):")
    x = -1.275
    y = 0.0
    return [p, complex(x, y)]

def RadiusOfSet(p, c):
    x0 = c.real
    y0 = c.imag
    r = 0.0
    k = 0.0
    while k<(x0*x0+y0*y0)**.5:
        r += .01
        k = r**p-r
    return r

def Escapes(z, p, c, R):
    t = (z**p)+c
    if abs(t) < R:
        return t
    else:
        return False

def linear_interpolation(a, b, t):
    return a * (1- t) + b * t


print("Width Divisors:")
W = 1000
print("Height Divisors:")
H = 1000
print("Iteration CHecks:")
N = 500

Julia = JuliaPoly();
Radius = RadiusOfSet(Julia[0], Julia[1])
const = Julia[1]
power = Julia[0]


setwindowsize(W, H)

p=0
while p < W:
    q = 0
    while q < H:
        i=0
        zpq = complex(-Radius+p*(2*Radius)/W, Radius-q*(2*Radius)/H)
        check = Escapes(zpq, power, const, Radius)
        while check and i<N:
            if type(check) == bool:
                break;
            else:
                check = Escapes(check, power, const, Radius)
                i+=1

        drawpixel(p, q, (i/N,i/N,i/N), 1)
        q+=1
    p+=1
    showimage()

showimage()
turtle.done()