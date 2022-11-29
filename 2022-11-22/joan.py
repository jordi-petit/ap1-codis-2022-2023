from dataclasses import dataclass
from typing import TypeAlias

@dataclass
class Provincia:
    nom: str
    capital: str
    habitants: int
    area: int
    pib: float

@dataclass
class Pais:
    nom: str
    capital: str
    provincies: list[Provincia]

Paisos: TypeAlias = list[Pais]

def pib(paisos: Paisos, inicial: str, densitat: float) -> float: 
    sumapib: float = 0.0
    for pais in paisos:
        for provincia in pais.provincies:
            sumapib += (provincia.pib if (provincia.habitants / provincia.area) > densitat and pais.nom[0] == inicial else 0)
    return sumapib
