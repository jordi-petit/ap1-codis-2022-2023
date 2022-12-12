"""Resolució de Sudokus"""


from dataclasses import dataclass
from typing import Optional, TypeAlias
from yogi import read


Usats: TypeAlias = list[list[bool]]


@dataclass
class Sudoku:
    graella: list[list[Optional[int]]]
    files: Usats
    columnes: Usats
    caixes: Usats


def escriure(s: Sudoku) -> None:
    for i in range(9):
        for j in range(9):
            if s.graella[i][j] is None:
                print(".", end=' ')
            else:
                print(s.graella[i][j], end=' ')
        print()
    print()
    if False:
        escriure_marques(s.files)
        escriure_marques(s.columnes)
        escriure_marques(s.caixes)


def escriure_marques(m: Usats) -> None:
    for i in range(9):
        for j in range(1, 10):
            if m[i][j]:
                print(j, end="")
            else:
                print("-", end="")
        print()
    print()


def crear() -> Sudoku:
    graella: list[list[Optional[int]]] = [[None for _ in range(9)] for _ in range(9)]
    files = [[False for _ in range(10)] for _ in range(9)]
    columnes = [[False for _ in range(10)] for _ in range(9)]
    caixes = [[False for _ in range(10)] for _ in range(9)]
    return Sudoku(graella, files, columnes, caixes)


def llegir() -> Sudoku:
    s = crear()
    for i in range(9):
        for j in range(9):
            v = read(str)
            if v != ".":
                marcar_casella(s, i, j, int(v))
    return s


def marcar_casella(s: Sudoku, i: int, j: int, v: int):
    s.graella[i][j] = v
    s.files[i][v] = True
    s.columnes[j][v] = True
    s.caixes[caixa(i, j)][v] = True


def desmarcar_casella(s: Sudoku, i: int, j: int, v: int):
    s.graella[i][j] = None
    s.files[i][v] = False
    s.columnes[j][v] = False
    s.caixes[caixa(i, j)][v] = False


def caixa(i: int, j: int) -> int:
    return 3*(i//3) + j//3


def seguent(i: int, j: int) -> tuple[int, int]:
    si = i
    sj = j + 1
    if sj == 9:
        si, sj = si+1, 0
    return si, sj


def resol_rec(s: Sudoku, i: int, j: int) -> bool:
    if i == 9:
        return True

    si, sj = seguent(i, j)

    if s.graella[i][j] is not None:
        return resol_rec(s, si, sj)
    else:
        for v in range(1, 10):
            if legal(s, i, j, v):
                marcar_casella(s, i, j, v)
                if resol_rec(s, si, sj):
                    return True
                desmarcar_casella(s, i, j, v)
        return False


def legal(s: Sudoku, i: int, j: int, v: int) -> bool:
    return not s.files[i][v] and not s.columnes[j][v] and not s.caixes[caixa(i, j)][v]


def resol(s: Sudoku) -> bool:
    return resol_rec(s, 0, 0)


def main() -> None:
    """Programa principal."""

    s: Sudoku = llegir()
    if resol(s):
        escriure(s)
    else:
        print('Sense solució')


if __name__ == '__main__':
    main()
