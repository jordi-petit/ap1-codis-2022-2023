import yogi
from typing import List


def print_permutacio(permutacio: List[str]) -> None:
    print("(", end="")
    print(*permutacio, sep=",", end="")
    print(")")


def genera_permutacions_fixant(i: int, permutacio_actual: List[str],
                                usats: List[bool], words: List[str], n: int) -> None:
    """Genera totes les permutacions possibles amb les paraules a words, donat
    que hem fixat els primers i elements que els tenim guardats a permutacio_actual
    i usats ens indica quins indexos de words s'han utilitzat per fer la permutacio actual.
    """
    if i == n:
        print_permutacio(permutacio_actual)
    else:
        for idx, elem_usat in enumerate(usats):
            if not elem_usat:
                permutacio_actual[i] = words[idx]
                usats[idx] = True
                genera_permutacions_fixant(i+1, permutacio_actual, usats, words, n)
                usats[idx] = False



def genera_permutacions(n: int, words: List[str]) -> None:
    usats = [False for i in range(n)]
    permutacio_actual = [" " for i in range(n)]
    genera_permutacions_fixant(0, permutacio_actual, usats, words, n)


def main():
    n = yogi.read(int)
    words: List[str] = list()
    for i in range(n):
        words.append(yogi.read(str))

    genera_permutacions(n, words)


if __name__ == "__main__":
    main()