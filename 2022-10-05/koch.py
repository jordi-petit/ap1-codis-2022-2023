
from turtle import *
from yogi import read


def koch(n: int, d: float) -> None:
    """Dibuixa la fractal de koch amb n nivell i distància d."""
    if n == -1:
        forward(d)
    else:
        koch(n - 1, d / 3)
        left(60)
        koch(n - 1, d / 3)
        right(120)
        koch(n - 1, d / 3)
        left(60)
        koch(n - 1, d / 3)


def floc_koch(n: int, d: float) -> None:
    """Dibuixa el floc de neu de Koch amb n nivell i distància d."""
    for _ in range(3):
        koch(n, d)
        right(120)


if __name__ == '__main__':
    left(90)
    hideturtle()
    speed(0)
    floc_koch(2, 200)
    done()
