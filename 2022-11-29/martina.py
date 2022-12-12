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
    """
    Retorna la suma del pib de les províncies que tenen una densitat major 
    a la donada dels països que comencen per una lletra inicial concreta.
    """

    suma = 0.0

    for Pais in paisos:
        if Pais.nom[0] == inicial:
            for Provincia in Pais.provincies:
                if Provincia.habitants/Provincia.area > densitat:
                    suma += Provincia.pib

    return suma



