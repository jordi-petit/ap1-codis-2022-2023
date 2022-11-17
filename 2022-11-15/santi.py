from yogi import read, tokens

paraula = list(read(str))
lletra_del_mig = paraula[0]
punts = 0
num_paraules = 0
llista_definitiva = []

def lletres_contingudes(paraula: list[str], paraula_1: list[str]) -> bool:
    """retorna un boolea conforme totes les lletres de la paraula_1 pertanyen a paraula"""
    for x in paraula_1:
        if x in paraula:
            pass
        else:
            return False
    return True

for paraula_1 in tokens(str):
    p = paraula_1
    paraula_1 = list(paraula_1)
    lletres = lletres_contingudes(paraula, paraula_1)
    if (len(paraula_1) >= 3) and (lletra_del_mig in paraula_1) and (lletres == True):     
        llista_definitiva.append(p)
        num_paraules = num_paraules + 1
        if len(paraula_1) == 3:
            punts = punts + 1
        elif len(paraula_1) == 4:
            punts = punts + 2
        else:
            punts = punts + len(paraula_1)
            tuti = lletres_contingudes(paraula_1, paraula)
            if tuti == True:
                punts = punts + 10

llista_definitiva = sorted(llista_definitiva)

for x in llista_definitiva:
    print(x)
print(5*'-')
print(punts)