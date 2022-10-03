def suma1seg(h: int, m: int, s: int) -> tuple[int, int, int]:
    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24:
                h = 0
    return h, m, s


def suma1seg2(hora: tuple[int, int, int]) -> tuple[int, int, int]:
    h, m, s = hora
    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24:
                h = 0
    return h, m, s


def main() -> None:
    h, m, s = 23, 59, 59
    h, m, s = suma1seg(h, m, s)
    print(h, m, s)


def main2() -> None:
    hora = 23, 59, 59
    hora = suma1seg2(hora)
    print(hora)


main2()
