import yogi


def gira_nombre(n: int) -> int:
    """Gira el nombre n retornant un enter. Assumim que n no acaba en 0."""
    resultat = 0
    while  n > 0:
        resultat *= 10
        resultat += n % 10
        n //= 10
    return resultat


def condicio_facil(d1: int, d2: int) -> bool:
    """Comprova que ni d1 ni d2 son digits que fan que automaticament un
    nombre no sigui estrobogramatic (2, 3, 4, 5 o 7)
    """
    return d1 == 2 or d1 == 3 or d1 == 4 or d1 == 5 or d1 == 7 \
           or d2 == 2 or d2 == 3 or d2 == 4 or d2 == 5 or d2 == 7


def condicio_estrobogrammatica(d1: int, d2: int) -> bool:
    """Comprova si els dos digits son iguals i diferents a 6 o 9, o si
    son l'un 6 i l'altre 9, o al reves.    
    """
    return d1 == d2 and d1 != 6 and d1 != 9 or d1==6 and d2==9 or d1==9 and d2 == 6


def strobogrammatic(nombre: int) -> bool:
    """Comprova si un nombre es estrobogramatic."""
    if nombre % 10 == 0 and nombre != 0:  # cas que ho veiem rapid i ens assegurem que podem girar el nombre.
        return False
    num_reves = gira_nombre(nombre)
    while nombre > 0:
        d1 = nombre % 10
        d2 = num_reves % 10
        if not condicio_estrobogrammatica(d1, d2) or condicio_facil(d1, d2):
            return False
        nombre //= 10
        num_reves //= 10
    return True

def main():
    senars = 0
    n = yogi.scan(int)
    while n is not None:
        if strobogrammatic(n):
            if n % 2 != 0:
                senars += 1
            print(f"{n} si es estrobogramatic")
        else:
            print(f"{n} no es estrobogramatic")
        n = yogi.scan(int)
    print()
    print(f"estrobogramatics senars: {senars}")

if __name__ == "__main__":
    main()
