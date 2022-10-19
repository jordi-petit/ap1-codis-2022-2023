import turtle
import yogi


def draw_circle_from_center(r: int):
    """This function draws a circle of radius r centered in the position where
    the turtle is before the call. Leaves the turtle in the same state before
    the call.
    """
    turtle.up()
    turtle.right(90)
    turtle.forward(r)
    turtle.left(90)
    turtle.down()
    turtle.circle(r)
    turtle.up()
    turtle.left(90)
    turtle.forward(r)
    turtle.right(90)
    turtle.down()


def draw_circles(n: int, d: float) -> None:
    """Draw the fractal with n levels and size d. Leaves the turtle in
    the same state before the call.
    """
    if n == 1:  # base case
        draw_circle_from_center(d)
    elif n > 1:  # recursive case
        draw_circle_from_center(d)
        for i in range(4):
            turtle.up()
            turtle.forward(d + d/2)
            turtle.down()
            draw_circles(n-1, d / 2)
            turtle.up()
            turtle.backward(d + d/2)
            turtle.left(90)
            turtle.down()


def main():
    n = yogi.read(int)
    d = yogi.read(float)

    draw_circles(n, d)
    turtle.done()


if __name__ == "__main__":
    main()
