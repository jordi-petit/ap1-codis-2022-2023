from turtle import*

speed(0)
bgcolor(0,0,0)

def shape (order, side, radio):
    if order > 0:
        pencolor(0.9098, 1/(order*2), 0.9725)
        for i in range(0, int(side)):
            circle(radio, 360/(side*2))
            right(720/side)
            if (i%4 == 0):
                forward(-radio)
                shape(order - 1, side/2, radio/1.5)
                pencolor(0.9098, 1/(order*2), 0.9725)
                forward(radio)
            right(720/side)
            circle(radio, 360/(side*2))
            right(720/side)


penup()
goto(0, 50)
pendown()

shape(4, 32, 200)

canvas = getcanvas()
canvas.postscript(file="resultat_turtle.ps", colormode='color')
done()
