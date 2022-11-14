from tkinter import Scale
import turtle

class patern:
    def __init__(self,tortoise, x, y, scale, angle,nestinglevel):
        self.tortoise = tortoise
        self.x = x
        self.y = y
        self.scale = scale
        self.angle = angle
        self.nestinglevel = nestinglevel
        self.growpoints = []
        self.childs = []
        self.r = 1
        self.g = 1-scale
        self.b = 1-scale

        self.doPatern()


    def setGrowthPoint(self, angleDiff):
        self.growpoints.append({'x':self.tortoise.xcor(), 'y': self.tortoise.ycor(), 'angle': self.tortoise.heading() + angleDiff})

    def poligon(self, size, faces):
        for i in range(faces):
            self.tortoise.forward(size)
            self.tortoise.left(360/(faces))
            if (i+1)%2 == 0:
                self.setGrowthPoint(0)

    def doPatern(self):
        self.tortoise.hideturtle()
        self.tortoise.penup()
        self.tortoise.setpos(self.x, self.y)
        self.tortoise.right(self.tortoise.heading()-self.angle)
        self.tortoise.pendown()
        self.tortoise.fillcolor(self.r, self.g, self.b)
        #self.tortoise.color( (self.r, self.g, self.b) )
        self.tortoise.begin_fill()
        self.tortoise.penup()
       
        self.tortoise.pendown()
        self.poligon(480*self.scale,6)
        self.tortoise.end_fill()
        self.doChilds()

    def doChilds(self):
        if self.nestinglevel == 0:
            return
        for point in self.growpoints:
            newbranch = patern(self.tortoise, point['x'], point['y'], self.scale*0.5, point['angle'],  self.nestinglevel-1)
            self.childs.append( newbranch)

tim = turtle.Turtle()
turtle.colormode(1)
turtle.tracer(8, 50)
turtle.width(1)
tim.penup()
tim.setpos(-300,-420)
parent = patern(tim,tim.xcor(),tim.ycor(),1,0,8)
tim.hideturtle()
input()


