from yogi import tokens, read

def llegir_dades(n:int) -> list[float]:
    L = []
    for x in range(n):
        x = read(float)
        L.append(x)
    return L


def diferencia(v1: list[float], v2: list[float]) -> list[float]:
    v = []
    aparicions = 0
    for i in range(len(v1)):
        if i == 0:
            for j in range(len(v2)):
                if v1[i] == v2[j]:
                    aparicions = aparicions + 1
            if aparicions == 0:
                v.append(v1[i])
            aparicions = 0
        else:
            if v1[i] != v1[i-1]:
                for j in range(len(v2)):
                    if v1[i] == v2[j]:
                        aparicions = aparicions + 1
                    if v1[i] < v2[j] or aparicions == 1:                     #Cambi 1: break cuan es més petit
                        break
                if aparicions == 0:
                    v.append(v1[i])
                aparicions = 0
    return(v)

def main()-> None:
    n1 = read(int)    
    v1 = llegir_dades(n1)
    n2 = read(int)
    v2 = llegir_dades(n2)
  
    print(diferencia(v1,v2))

if __name__ == "__main__":
    main()