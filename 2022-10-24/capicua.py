def capicua(L: list[int]) -> bool:
    """Indica si L és capicua."""

    # return L == list(reversed(L))

    n = len(L)
    for i in range(n // 2):
        if L[i] != L[n - 1 - i]:
            return False
    return True


print(capicua([4, 5, 5, 4]))
print(capicua([4, 5, 2, 5, 4]))
