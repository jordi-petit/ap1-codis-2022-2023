
def es_primer(n: int) -> bool:
    """Indica si el natural és primer o no."""

    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


for i in range(30):
    if es_primer(i):
        print(i)
