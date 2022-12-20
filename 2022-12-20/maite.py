from yogi import read, scan


def traduir(alf: list[str], taula: str, text: str) -> None:
    """Escriu el text original donat un de xifrat."""

    for i in range(len(text)):
        if text[i] == '_':
            print(' ', end='')
        else:
            print(alf[trobar_index(taula,text[i])], end='')


def trobar_index(taula: str, lletra: str) -> int:
    """Retorna l'index a l'alfabet comú d'una lletra del text."""

    for i in range(len(taula)):
        if lletra == taula[i]:
            return i


def main() -> None:

    alfabet = [chr(x) for x in range(97,123)]
    taula = scan(str)
    n = scan(int)

    while taula is not None and n is not None:
        for _ in range(n):
            text = read(str)
            traduir(alfabet, taula, text)
            print()
        
        print()
        taula = scan(str)
        n = scan(int)


if __name__ == '__main__':
    main()