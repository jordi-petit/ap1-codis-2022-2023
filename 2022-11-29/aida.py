from yogi import scan
from typing import TypeAlias

Fila: TypeAlias = list[int]
Matriu: TypeAlias = list[Fila]

def fes_espiral(G: Matriu, n:int, iteracio: int)->None:
    if n > iteracio*2:
        for i in range (iteracio,n - iteracio):
            G[n-1-iteracio][i] ='X' # pintem fila de baix
            G[i][n-1-iteracio] = 'X' # pintem columna dreta
            if i > iteracio:
                G[iteracio][i] = 'X' # pintem fila de dalt
            if i < n-2-iteracio:
                G[i][iteracio+1] = 'X' # pintem columna esquerra

        fes_espiral(G,n, iteracio+2)

def pinta_espiral(G: Matriu, n:int)-> None:
    for i in range(n):
        print(*G[i], sep = "")
        
def main()->None:
    n = scan(int)
    while n != 0:
        G = [['.' for _ in range (n)] for _ in range (n)]
        fes_espiral(G,n,0)
        pinta_espiral(G,n)
        print()
        n = scan(int)

main()
