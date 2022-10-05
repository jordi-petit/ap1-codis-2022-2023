

from turtle import *
from yogi import read


def arbre(n: int, d: float, a: float) -> None:
    """
    Dibuixa un arbre fractal d'n nivell, distància d i angle a,
    tot deixant la tortuga a la posició i orientació inicial.
    """
    if n == 0:
        forward(d)
        backward(d)
    else:
        forward(d)
        left(a / 2)
        arbre(n - 1, d * 3 / 4, a)
        right(a)
        arbre(n - 1, d * 3 / 4, a)
        left(a / 2)
        backward(d)


if __name__ == '__main__':
    left(90)
    hideturtle()
    speed(0)
    arbre(5, 100, 60)
    done()
