
def factorial(n: int) -> int:
    """Retorna el factorial d'un natural n."""

    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f


def main() -> None:
    for i in range(10):
        print(i, factorial(i))


if __name__ == '__main__':
    main()
