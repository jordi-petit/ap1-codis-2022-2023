# programa que escriu tots els divisors d'un nombre natural (versió lenta)

from yogi import read

n = read(int)
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i = i + 1
