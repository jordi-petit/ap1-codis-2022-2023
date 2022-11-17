
def difference(v1: list[float], v2: list[float]) -> list[float]:
    """ Funció que retorna la diferència de taules de dos vectors """

    diff: list[float] = []

    n, m = len(v1), len(v2)
    i, j = 0, 0

    while i < n and j < m:
        if v1[i] < v2[j]:
            if i == 0 or v1[i] != v1[i - 1]:
                diff.append(v1[i])
            i += 1
        elif v1[i] > v2[j]:
            j += 1
        else:
            i += 1
            j += 1
        
    if i < n:
        for x in range(i, n):
            if x == 0 or v1[x] != v1[x - 1]:
                diff.append(v1[x])
    
    return diff

def main() -> None:

    v1: list[float] = [1, 2, 2, 5, 5, 7]
    v2: list[float] = [2, 3, 3, 7]

    print(difference(v1, v2))


if __name__ == '__main__':
    main()

