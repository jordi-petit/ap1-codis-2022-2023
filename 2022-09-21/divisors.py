
def escriure_divisors(n: int) -> None:
    d = 1
    while d*d < n:
        if n % d == 0:
            print(d)
        d = d + 1
    if d * d == n:
        print(d)
    while d >= 2:
        d = d - 1
        if n % d == 0:
            print(n // d)


escriure_divisors(56)
