import random
import time
from typing import Any


def mergesort(L: list[Any]) -> None:
    """Ordena la llista L per fusió."""

    mergesort_rec(L, 0, len(L) - 1)


def mergesort_rec(L: list[Any], esq: int, dre: int) -> None:
    """Ordenar L[esq..dre]."""

    if esq < dre:
        mig = (esq + dre) // 2
        mergesort_rec(L, esq, mig)
        mergesort_rec(L, 1 + mig, dre)
        merge(L, esq, mig, dre)


def merge(L: list[Any], esq: int, mig: int, dre: int) -> None:
    """
    Ordena L[esq..dre] sabent que L[esq..mig] està ordenat
    i sabent que L[mig+1..dre] està ordenat.
    """

    R = L[0:0]  # això és el mateix que R = [] però així mypy no plora
    i = esq
    j = mig + 1
    while i <= mig and j <= dre:
        if L[i] <= L[j]:
            R.append(L[i])
            i += 1
        else:
            R.append(L[j])
            j += 1
    R.extend(L[i:mig + 1])
    R.extend(L[j:dre + 1])
    L[esq:dre + 1] = R


def main() -> None:
    """Mesura el temps per ordenar llistes amb elements aleatoris."""

    for n in range(50000, 1000001, 50000):
        L = [random.randint(0, n) for _ in range(n)]
        t1 = time.perf_counter()
        mergesort(L)
        t2 = time.perf_counter()
        print(n, t2 - t1)


main()
