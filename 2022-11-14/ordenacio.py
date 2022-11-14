from yogi import tokens
import itertools
import random
import time
from typing import Any


def ordena_sel(L: list[Any]) -> None:
    """Ordena la llista L per selecció."""

    n = len(L)
    for i in range(n):
        p = posicio_minim(L, i)
        L[i], L[p] = L[p], L[i]


def posicio_minim(L: list[Any], i: int) -> int:
    """Retorna la posició del mínim de L[i:]."""

    n = len(L)
    p = i
    for j in range(i + 1, n):
        if L[j] < L[p]:
            p = j
    return p


def ordena_ins(L: list[Any]) -> None:
    """Ordena la llista L per inserció."""

    n = len(L)
    for i in range(1, n):
        insereix(L, i)


def insereix(L: list[Any], i: int) -> None:
    """Insereix ordenadament L[i] en L[:i+1] sabent que L[:i] està ordenada."""

    x = L[i]
    j = i - 1
    while j >= 0 and L[j] > x:
        L[j+1] = L[j]
        j -= 1
    L[j + 1] = x


def insereix_antic(L: list[Any], i: int) -> None:
    """Insereix l'element L[i] en la llista L[:i+1] sabent que L[:i] està ordenada."""

    j = i - 1
    while j >= 0 and L[j] > L[j + 1]:
        L[j], L[j+1] = L[j+1], L[j]
        j -= 1


def main1() -> None:
    """Llegeix una llista d'enters i l'escriu ordenada."""

    L = list(tokens(int))
    ordena_sel(L)
    print(L)


def main2() -> None:
    """Ordena totes les permutacions d'n elements amb n fins a 10."""

    c = 0
    for n in range(10):
        for permutacio in itertools.permutations(range(n)):
            c = c + 1
            L = list(permutacio)
            ordena_sel(L)
            if L != list(range(n)):
                print('cagada', permutacio)
    print(c)


def main3() -> None:
    """Mesura el temps per ordenar llistes amb elements aleatoris."""

    for n in range(1000, 20001, 1000):
        L = [random.randint(0, n) for _ in range(n)]
        t1 = time.perf_counter()
        ordena_ins(L)
        t2 = time.perf_counter()
        print(n, t2 - t1)


if __name__ == '__main__':
    main3()
