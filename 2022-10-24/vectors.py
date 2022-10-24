import math


def producte_escalar(x: list[float], y: list[float]) -> float:
    """Retorna  el producte escalar de dos vectors x i y de la mateixa mida."""

    n = len(x)
    s = 0.0
    for i in range(n):
        s += x[i] * y[i]
    return s


def modul(x: list[float]) -> float:
    """Retorna el mòdul d'un vector."""

    return math.sqrt(producte_escalar(x, x))


def perpendiculars(x: list[float], y: list[float]) -> bool:
    """Diu si x i y són vectors perpendiculars."""

    return abs(producte_escalar(x, y)) < 1e-12


def doblar(x: list[float]) -> None:
    """Dobla el valor dels components de x."""

    for i in range(len(x)):
        x[i] *= 2

    # no funciona:
    # for element in x:
    #    element *= 2


def afegeix_suma(L: list[int]) -> None:
    """Afegeix a L un element al final que és la suma dels elements en L."""

    L.append(sum(L))

    # no funciona: L = L + [sum(L)]


def main():
    # print(producte_escalar([1, 2, 3], [4, 5, 6]))
    a = [1, 2, 3]
    afegeix_suma(a)
    print(a)


main()
