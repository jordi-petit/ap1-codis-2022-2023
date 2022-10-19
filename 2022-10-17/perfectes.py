def es_primer(n: int) -> bool:
    if n <= 1:
        return False
    c = 2
    while c * c <= n:
        if n % c == 0:
            return False
        c = c + 1
    return True


def suma_digits(n: int) -> int:
    if n < 10:
        return n
    else:
        return suma_digits(n // 10) + n % 10


def es_primer_perfecte(n: int) -> bool:
    return (n < 10 or es_primer_perfecte(suma_digits(n))) and es_primer(n)
