from yogi import read, scan

# lletra del mig obligatoria.
# minim de 3 lletres.
# 3 lletres -> 1 punt / 4 lletres -> 2 punts
# a partir de 5 lletres, tants punts com lletres tingui la paraula.
# tuti -> 10 punts extra!

def conte_primera(paraula: str, lletres: str) -> bool: 
    """Ens diu si la nostra paraula conté la primera lletra de la referència, és a dir, la del mig (vermella)."""

    conte = False
    for l in paraula:
        if l == lletres[0]:
            conte = True
    return conte

def conte_lletra_invalida(paraula: str, lletres: str) -> bool:
    """Ens diu si la paraula donada conté una lletra diferent a les de referència."""
    
    conte_li = False
    for l in paraula:
        if l not in lletres:
            conte_li = True
    return conte_li

def valida(paraula: str, lletres: str) -> bool:
    """Ens diu si la paraula introuïda compleix les condicions de validesa del paraulògic."""

    if len(paraula) < 3:
        return False
    
    if not conte_primera(paraula, lletres):
        return False 
    
    if conte_lletra_invalida(paraula, lletres):
        return False
    return True

def conte_totes(paraula: str, lletres: str) -> bool:
    """Ens diu si una paraula conté totes les lletres de la paraula de referència."""

    for l in lletres:
        if not l in paraula:
            return False
    return True

def comptar_punts(paraula: str, lletres: str) -> int:
    """Compta els punts de cada paraula vàlida."""

    s = 0 # suma de punts
    if len(paraula) == 3:
        s += 1
    elif len(paraula) == 4:
        s += 2
    elif len(paraula) > 4:
        s += len(paraula)
        if conte_totes(paraula, lletres):
            s += 10 
    return s
    
def main() -> None:
    compt = 0
    valides: list[str] = list()
    lletres = read(str) # str que conté totes les lletres possibles per formar paraules
    paraula = scan(str)
    while paraula is not None:
        if valida(paraula, lletres):
            compt += comptar_punts(paraula, lletres)
            valides.append(paraula)
        paraula = scan(str)
    valides.sort()
    for n in valides:
        print(n)
    print("-----")
    print(compt)
    
if __name__ == '__main__':
    main()

