# programa que calcula el factorial d'un nombre natural

from yogi import read

n = read(int)
i = 1
f = 1
while i <= n:
    f = f * i
    i = i + 1
print(f)
