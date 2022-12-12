import yogi


def generar_permutacions(n: int) -> None:
    """Escriu totes les permutacions de llargada n"""

    L = [-1 for _ in range(n)]
    usat = [False for _ in range(n)]
    generar_permutacions_rec(n, L, 0, usat)


def generar_permutacions_rec(n: int, L: list[int], i: int, usat: list[bool]) -> None:
    """Escriu totes les permutacions de llargada n que comencin amb L"""

    if n == i:
        print(*L)
    else:
        for k in range(n):
            if not usat[k]:
                L[i] = k
                usat[k] = True
                generar_permutacions_rec(n, L, i + 1, usat)
                usat[k] = False


def main() -> None:
    n = yogi.read(int)
    generar_permutacions(n)


main()
