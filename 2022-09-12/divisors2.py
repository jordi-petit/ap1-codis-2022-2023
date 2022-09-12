# programa que escriu tots els divisors d'un nombre natural (versió ràpida)

from yogi import read

n = read(int)
i = 1
while i * i < n:
    if n % i == 0:
        print(i, n // i)
    i = i + 1
if i * i == n:
    print(i)
