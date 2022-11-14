from math import *
from turtle import *

#A function that changes the color of the petals on each iteration.
#Values were chosen based on aesthetics through a process of trial and error


def redgreenblue(red, green, blue):
    
    if red > 0.9:
        if blue >= 0.1:
            blue -= 0.1
        elif green <= 0.8:
            green += 0.2
        else:
            red -= 0.1
    elif green > 0.8:
        if red >= 0.2:
            red -= 0.2
        elif blue <= 0.8:
            blue += 0.2
        else:
            green -= 0.1
    else:
        if green >= 0.2:
            green -= 0.2
        else:
            red += 0.1
    return red, green, blue


#A function that draws a flower were 'size' is the the radius of the biggest circle completely contained within 
#the flower and 'petals' the number of petals of the flower

def flower(size, petals):
    
    for _ in range(petals):
        
        begin_fill()
        forward(size)
        circle(size * tan(halfangle), 180 + 360/petals)
        forward(size)
        right(180)
        end_fill()
        
#Draws the fractal. 'n' is the number of iterations, 'r', 'g', and 'b', the values of the color of each iteration and 'i'
#a value related to the width of the border of each petal 

def recursive_flower(size, petals, n, r, g, b, i):

    
    if(n > 0):
        
        n -= 1
        width(i//2)
        if i > 1:
            i -= 1
        r, g, b = redgreenblue(r, g, b)
        fillcolor(r, g, b)
        flower(size, petals)
        right(180/petals) #On each iteration the flower rotates by half of the angle between two petals...
        recursive_flower(size/(((tan(halfangle))*(1+sin(halfangle)))+cos(halfangle)), petals, n, r, g, b, i) 
        #... and decreases by a certain trigonometric factor such that the next flower is perfectly contained within the last


size = int(input("How big in pixels do you want the starting  petal size to to be? ")) #Suggested: 1050 pixels
petals = int(input("How many petals should it have? ")) #Suggested: 50 petals
n = int(input("How many iterations? ")) #Suggested: 80 iterations

halfangle = pi/petals #Half of the angle that separates two petals, in radians
r = 0.9
g = 0.0
b = 0.0
i = 30

hideturtle()
speed(0)

recursive_flower(size, petals, n, r, g, b, i)

canvas = getcanvas()
canvas.postscript(file="resultado_turtle.ps", colormode ='color')
done()
