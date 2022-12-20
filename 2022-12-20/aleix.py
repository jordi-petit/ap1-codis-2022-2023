from yogi import read
def veins(m:list[list[int]], i:int, j:int)->int:
    """Retorna el nombre de veïns que té una casella."""
    suma = 0
    ii = i
    ji = j
    for i in range(max(0, ii-1), min(ii+2, len(m))):
        for j in range(max(0, ji-1), min(ji+2, len(m[0]))):
            if not(i == ii and j == ji):
                if m[i][j] == "B":
                    suma += 1
    return suma
def main()->None:
    fila, columna = read(int),read(int)
    while fila != 0:
        matriu_t = [list(read(str)) for _ in range(fila)]
        matriu_tseguent = [[ "." for _ in range(columna)] for _ in range(fila)]
        
        for j in range(columna):
            for i in range(fila):
                if matriu_t[i][j] == "." and veins(matriu_t,i,j) == 3:
                    matriu_tseguent[i][j] = "B"
                elif matriu_t[i][j] == "B" and (veins(matriu_t,i,j) == 2 or veins(matriu_t,i,j) == 3):
                    matriu_tseguent[i][j] = "B"
        
        for i in range(fila):
            print(*[matriu_tseguent[i][j] for j in range(columna)],sep="")
        
        fila, columna = read(int),read(int)
        if fila!=0:
            print()

if __name__=="__main__":
    main()
