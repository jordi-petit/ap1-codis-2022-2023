
from typing import Optional


def cerca_binaria(L: list[int], x: int) -> Optional[int]:
    """
    Si x és a L, retorna una posició i tal que L[i] = x.
    Si x no és a L, retorna None.

    Prec: L està ordenada.

    Temps: logarítmic en la mida de L.
    """

    n = len(L)
    esq, dre = 0, n - 1
    while esq <= dre:
        mig = (esq + dre) // 2
        if x < L[mig]:
            dre = mig - 1
        elif x > L[mig]:
            esq = mig + 1
        else:  # x == L[mig]
            return mig
    return None


print(cerca_binaria([4, 6, 7, 7, 9, 11, 13], 12))
print(cerca_binaria([4, 6, 7, 7, 9, 11, 13], 11))
