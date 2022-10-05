

def suma_digits(n: int) -> int:
    """Donat un natural n, retorna la suma dels seus dígits (en base 10)."""

    if n == 0:
        return 0
    else:
        return n % 10 + suma_digits(n // 10)


if __name__ == '__main__':
    print(suma_digits(5618))
