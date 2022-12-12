import yogi


def generar_combinacions(n: int, k: int) -> None:
    """Escriu totes les combinacions de llargada n amb 0s i 1s amb k 1s"""

    L = [-1 for _ in range(n)]
    generar_combinacions_rec(n, L, 0, k)


def generar_combinacions_rec(n: int, L: list[int], i: int, k: int) -> None:
    """Escriu totes les combinacions de llargada n amb 0s i 1s que comencin amb L[:i] i que acabi amb k uns"""

    if k >= 0 and k <= n-i:
        if n == i:
            print(*L)
        else:
            L[i] = 0
            generar_combinacions_rec(n, L, i + 1, k)
            L[i] = 1
            generar_combinacions_rec(n, L, i + 1, k - 1)


def main() -> None:
    n = yogi.read(int)
    k = yogi.read(int)
    generar_combinacions(n, k)


main()
