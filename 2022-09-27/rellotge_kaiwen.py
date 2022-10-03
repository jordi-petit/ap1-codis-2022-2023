import turtle
from yogi import read

def dibuixa_rellotge() -> None:
    """Dibuixa un rellotge amb 12 ratlles"""
    turtle.penup()
    turtle.forward(200)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(200)
    turtle.penup()
    turtle.goto(0,0)
    for a in range(12):
        turtle.forward(150)
        turtle.pendown()
        turtle.forward(50)
        turtle.penup()
        turtle.goto(0,0)
        turtle.right(360/12)

def dibuixa_busca(h: int, m: int) -> None:
    """Dibuixa les busques del rellotge"""
    for i in range(2):   #quan i = 0 -> Dibuixa busca hores| quan i = 1 -> Dibuixa busca minuts
        turtle.right(((1-i) * (360/12) * (h + m/60)) + (i * (360/60) * m))
        turtle.pendown()
        turtle.forward(90 + 50 * i)
        turtle.right(150)
        turtle.forward(25)
        for b in range(2):
            turtle.right(120)
            turtle.forward(25)
        turtle.penup()
        turtle.goto(0,0)
        turtle.left(((1-i) * (360/12) * (h + m/60)) + (i * (360/60) * m) + 30)

def main() -> None:
    h = read(int)
    m = read(int)
    dibuixa_rellotge()
    dibuixa_busca(h, m)
    turtle.done()

if __name__ == "__main__":
    main()