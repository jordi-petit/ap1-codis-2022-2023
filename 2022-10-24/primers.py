
def es_primer(x: int) -> bool:
    """Donat un enter x >= 0, indica si és o no primer."""
    if x <= 1:
        return False
    c = 2
    while c * c <= x:
        if x % c == 0:
            return False
        c += 1
    return True


def garbell(n: int) -> list[bool]:
    """
    Retorna una llista L de n + 1 posicions 
    tal que L[i] és cert si i i només
    si i és un nombre primer.
    """

    L = [True for _ in range(n + 1)]
    L[0] = L[1] = False
    i = 2
    while i * i <= n:
        if L[i]:
            for j in range(2 * i, n + 1, i):
                L[j] = False
        i = i + 1
    return L


def llista_primers_lent(n: int) -> list[int]:
    """Retorna la llista de tots els primers fins a n. Prec n >= 0."""

    return [x for x in range(n + 1) if es_primer(x)]


def llista_primers(n: int) -> list[int]:
    """Retorna la llista de tots els primers fins a n. Prec n >= 0."""

    primers = garbell(n)
    return [x for x in range(n + 1) if primers[x]]


print(len(llista_primers(1000000)))
