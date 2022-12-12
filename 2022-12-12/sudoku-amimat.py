

from dataclasses import dataclass
from typing import Optional
from yogi import read
import blessings
import time

Graella = list[list[Optional[int]]]
"""Graella 9x9 per desar els valors (de 0 a 8 o None per "no se sap")."""


Usats = list[set[int]]
"""Vector de 9 subconjunts de {0..8} per indicar els valors usats."""


term = blessings.Terminal()
"""Per tenir coloraines i poder moure el cursor pel terminal."""


@dataclass
class Sudoku:
    """Classe per mantenir la informació d'un sudoku en construcció."""

    original: Graella  # la graella original
    graella: Graella  # la graella principal
    files: Usats  # conflictes per files
    columnes: Usats  # conflictes per columnes
    caixes: Usats  # conflictes per caixes


def crea() -> Sudoku:
    """Retorna un sudoku buit."""

    original: Graella = [[None for _ in range(9)] for _ in range(9)]
    graella: Graella = [[None for _ in range(9)] for _ in range(9)]
    files: Usats = [set() for _ in range(9)]
    columnes: Usats = [set() for _ in range(9)]
    caixes: Usats = [set() for _ in range(9)]
    return Sudoku(original, graella, files, columnes, caixes)


def llegir() -> Sudoku:
    """Llegeix i retorna un sudoku."""

    s = crea()
    for i in range(9):
        for j in range(9):
            v = read(str)
            if v != '.':
                ok = marcar_casella(s, i, j, int(v) - 1)
                assert ok
                s.original[i][j] = int(v) - 1
    return s


def escriure(s: Sudoku) -> None:
    for i in range(9):
        for j in range(9):
            v = s.graella[i][j]
            assert v is not None
            print(v + 1, end=' ')
        print()


def mostrar(s: Sudoku) -> None:
    for i in range(9):
        for j in range(9):
            v = s.graella[i][j]
            if v is None:
                print(term.move(i, j*2) + '.')
            elif s.original[i][j] == None:
                print(term.move(i, j*2) + str(v + 1))
            else:
                print(term.move(i, j*2) + term.bold(str(v + 1)))
    # time.sleep(0.01)


def marcar_casella(s: Sudoku, i: int, j: int, v: int) -> bool:
    """Si es pot posar el valor v en s[i][j] ho fa i retorna cert, sinó retorna fals."""

    if v in s.files[i] or v in s.columnes[j] or v in s.caixes[caixa(i, j)]:
        return False
    s.files[i].add(v)
    s.columnes[j].add(v)
    s.caixes[caixa(i, j)].add(v)
    s.graella[i][j] = v
    mostrar(s)
    return True


def desmarcar_casella(s: Sudoku, i: int, j: int) -> None:
    """Treu el valor de s[i][j]."""

    v = s.graella[i][j]
    assert v is not None
    s.files[i].remove(v)
    s.columnes[j].remove(v)
    s.caixes[caixa(i, j)].remove(v)
    s.graella[i][j] = None
    mostrar(s)


def caixa(i: int, j: int) -> int:
    """Retorna el número de caixa de la casella i,j."""

    return 3 * (i//3) + j // 3


def resol(s: Sudoku) -> bool:
    """Prova de resoldre el sudoku i indica si ho ha fet."""

    return resol_rec(s, 0, 0)


def resol_rec(s: Sudoku, i: int, j: int) -> bool:

    # cas base
    if i == 9:
        return True

    # calcular casella següent
    seg_i, seg_j = i, j + 1
    if seg_j == 9:
        seg_i, seg_j = seg_i + 1, 0

    if s.graella[i][j] is not None:
        # si la casella és coneguda, continuar per la casella següent
        return resol_rec(s, seg_i, seg_j)
    else:
        # provar tots els possibles valors
        for v in range(9):
            if marcar_casella(s, i, j, v):
                if resol_rec(s, seg_i, seg_j):
                    return True
                desmarcar_casella(s, i, j)
        return False


def main() -> None:
    """Programa principal."""

    print(term.clear() + term.hide_cursor())

    s = llegir()
    if resol(s):
        escriure(s)
    else:
        print('Sense solució')


if __name__ == '__main__':
    main()
