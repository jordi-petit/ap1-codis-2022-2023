from yogi import read

def suma_un_mes(mes: str) -> str:
    if mes == "gener":
        return "febrer"
    elif mes == "febrer":
        return "marc"
    elif mes == "marc":
        return "abril"
    elif mes == "abril":
        return "maig"
    elif mes == "maig":
        return "juny"
    elif mes == "juny":
        return "juliol"
    elif mes == "juliol":
        return "agost"
    elif mes == "agost":
        return "setembre"
    elif mes == "setembre":
        return "octubre"
    elif mes == "octubre":
        return "novembre"
    elif mes == "novembre":
        return "desembre"
    else:  # mes == "desembre"
        return "gener"


def es_any_de_traspas(any: int) -> bool:
    return any % 4 == 0 and (any % 100 == 0 and (any//100) % 4 == 0 or any % 100 != 0)


def ultim_dia_de_mes(dia: int, mes: str, any: int) -> bool:
    return dia == 31 and (mes == "gener" or mes == "marc" or mes == "maig" or \
        mes == "juliol" or mes == "agost" or mes == "octubre" or mes == "desembre") \
        or dia == 30 and (mes == "abril" or mes == "juny" or mes == "setembre" or mes == "novembre") \
        or dia == 28 and mes == "febrer"  and not es_any_de_traspas(any) \
        or mes == "febrer" and es_any_de_traspas(any) and dia == 29


def dia_seguent(dia: int, mes: str, any: int) -> tuple[int, str, int]:
    if ultim_dia_de_mes(dia, mes, any):
        dia = 1
        mes = suma_un_mes(mes)
        if mes == "gener":
            any += 1
    else:
        dia += 1
    return dia, mes, any


def main():
    for i in range(8):
        dia = read(int)
        mes = read(str)
        any = read(int)
        print(dia_seguent(dia, mes, any))


if __name__ == "__main__":
    main()