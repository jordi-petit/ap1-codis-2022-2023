def escriure_guions(n: int) -> None:
    """Escriu n guions per un nat n"""

    if n == 0:
        pass
    elif n == 1:
        print('-')
    else:
        escriure_guions(n // 2)
        escriure_guions(n - n // 2)


escriure_guions(7)
