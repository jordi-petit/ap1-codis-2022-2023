# programa que calcula el valor absolut d'un nombre

from yogi import read

x = read(int)
if x < 0:
    x = -x
print(x)
