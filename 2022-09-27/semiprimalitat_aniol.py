


def semiprimalitat(n:int):
    a = 2
    while a * a <= n:       #busquem divisors
        if n % a == 0:
            b = n // a
            c = 2
            while c * c <= b:   #busquem nombres primers
                if b % c == 0:
                    return None     # el divisor no és primer -> el nombre no és semiprimer
                c += 1  
            return (a, b)   #com que a serà sempre el que és més petit que l'arrel, i b el més gran, ja no ens preocupem per quin és mes gran
        a += 1





