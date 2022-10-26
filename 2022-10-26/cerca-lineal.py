
from typing import Optional


def cerca(L: list[int], x: int) -> Optional[int]:
    """
    Si x és a L, retorna una posició i tal que L[i] = x.
    Si x no és a L, retorna None.

    Temps: lineal en la mida de L.
    """

    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return None


print(cerca([11, 13, 4, 7, 2, 11, 13], 12))
print(cerca([11, 13, 4, 7, 2, 11, 13], 2))
