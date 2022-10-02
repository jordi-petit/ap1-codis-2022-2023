from yogi import read
from typing import Optional

def es_primer(n: int) -> bool:
    """Diu si el enter Ã©s primer."""
    if n <= 1:
        return(False)
    else:   
        d = 2
        while d * d <= n:
            if n % d == 0:
                return(False)
            else: d = d + 1
    return(True)

def semiprimalitat(n: int) -> Optional [tuple[int, int]]:
    if n <= 1:
        return(None)
    else:
        x = 2
        while n % x != 0:
            x = x + 1
        d = n // x
        if es_primer(d):
            if d > x:
                return (x, d)
            else: return (d, x)
        else: return(None)

def main():
    a = read(int)
    return (semiprimalitat(a))


if __name__ == "___main___":
    main()