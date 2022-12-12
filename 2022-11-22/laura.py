from yogi import *
def print_matriu(matriu: list[list[str]], n:int):
    """Imprimeix una matriu de mida nxn."""
    for i in range(n):
        for j in range(n):
            if j == n-1:
                print(matriu[i][j])
            else:
                print(matriu[i][j], end = '')
    print('')

def espirals(n: int) -> None:
    """Dibuixa una espiral en una matriu tractant cada segment per separat (avall, dreta, amunt, esquerre)."""
    i = 0 #files
    j = 0 #columnes
    matriu: list[list[str]] = [["X" for x in range(n)] for i in range(n)]
    count = n-1 #mida de cada segment
    while count > 0:
        for k in range(i, i + count): #avall
            matriu[k][j] = '.'
        i = k #comencem a la fila on ens havíem quedat
        j += 1 #pel nou segment no incloem al còmput l'última posició pintada en l'anterior segment
        count -= 1 #cada segment és més curt que l'anterior

        for k in range(j, j + count): #dreta
            matriu[i][k] = '.'
        j = k
        i -= 1
        count -= 1

        for k in range(i, i-count, -1): #amunt
            matriu[k][j] = '.'
        i = k
        count -= 1
        j -= 1

        for k in range(j, j-count, -1): #esquerre
            matriu[i][k] = '.'
        j = k
        i += 1
        count -= 1
    print_matriu(matriu, n)
  

def main():
    n = read(int)
    while n != 0:
        espirals(n)
        n = read(int)

if __name__ == '__main__':
    main()
