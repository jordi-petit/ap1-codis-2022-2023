from dataclasses import dataclass
from yogi import scan
from functools import cmp_to_key
 
@dataclass
class paraula:
    contingut: str
    vegades: int
 
def comparacio(p1: paraula, p2: paraula) -> int:
    """Aquesta funció compara dues paraules i retorna un valor positiu/negatiu per endreçar la llista"""
    if p1.vegades == p2.vegades:
        if p1.contingut > p2.contingut:
            return 1
        else:
            return -1
    if p1.vegades > p2.vegades:
        return -1 
    else: 
        return 1
 
def main():
    n = scan(int)
    k = scan(int)

    while n is not None:
        llista_paraules: list[str] = [scan(str) for _ in range(n)]
        llista_paraules.sort()
 
        numero_paraules: list[paraula] = []
        comptador = 1
 
        for i in range(1, n):
            if llista_paraules[i - 1] != llista_paraules[i]:
                numero_paraules.append(paraula(llista_paraules[i - 1], comptador))
                comptador = 1
            else: 
                comptador += 1
 
        numero_paraules.append(paraula(llista_paraules[-1], comptador))
 
        numero_paraules_ordenades = sorted(numero_paraules, key=cmp_to_key(comparacio))
 
        for i in range (k):
            print (numero_paraules_ordenades[i].contingut)
        print ('-' * 10)
 
        n = scan(int)
        k = scan(int)
 
if __name__ == '__main__':
    main()