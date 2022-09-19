from yogi import read


def maxim2(a: int, b: int) -> int:
    """Retorna el màxim de dos valors enters."""

    if a > b:
        return a
    else:
        return b


def maxim3(a: int, b: int, c: int) -> int:
    """Retorna el màxim de tres valors enters."""

    return maxim2(maxim2(a, b), c)


def factorial(n: int) -> int:
    """Donat un valor n positiu o zero, calcula el factorial de n."""

    n = read(int)
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f


def binomial(n: int, k: int) -> int:
    """Retorna el coeficient binomial (n k) amb 0 <= k <= n."""
    return factorial(n) // (factorial(k) * factorial(n - k))


def mitjana(a: float, b: float) -> float:
    """Retorna la mitjana de dos reals"""

    return (a + b) / 2


def main() -> None:
    """Programa principal"""
    n = read(int)
    k = read(int)
    c = binomial(n, k)
    print(c)


main()
