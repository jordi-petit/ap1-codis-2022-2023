def factorial(n: int) -> int:
    """Donat un natural n, retorna n!"""

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
