import turtle


def dibuixar_quadrat(x, y, distancia):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    for i in range(4):
        turtle.forward(distancia)
        turtle.left(90)
    turtle.up()

def fractal_recursiu(x, y, nivell, distancia):

    if nivell> 0:
        dibuixar_quadrat(x, y, distancia)

        fractal_recursiu(x + distancia, y + distancia, nivell -1, distancia/2)
        fractal_recursiu(x - distancia/2 , y+ distancia, nivell -1 , distancia/2)
        fractal_recursiu(x - distancia/2, y- distancia/2 , nivell -1, distancia/2)



print(fractal_recursiu(0,0,2,50))
turtle.done()
