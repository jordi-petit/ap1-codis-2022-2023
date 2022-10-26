from yogi import tokens


def llegir_dades() -> list[int]:
    L = []
    for x in tokens(int):
        L.append(x)
    return L


def comptar_ocurrencies(llista: list[int], element: int) -> int:
    c = 0
    for x in llista:
        if x == llista[-1]:
            c += 1
    return c


def main() -> None:
    L = llegir_dades()
    print(comptar_ocurrencies(L, L[-1]))


main()
