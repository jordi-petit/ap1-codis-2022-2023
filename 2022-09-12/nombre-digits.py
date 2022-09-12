# programa que calcula el nombre de dígits d'un nombre natural

from yogi import read

n = read(int)
if n == 0:
    d = 1
else:
    d = 0
    while n != 0:
        d = d + 1
        n = n // 10
print(d)
