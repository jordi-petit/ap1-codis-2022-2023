# programa que escriu els nombres de 1 a n.
# programa que calcula la suma dels dígits d'un nombre natural

from yogi import read

n = read(int)
s = 0
while n != 0:
    s = s + n % 10
    n = n // 10
print(s)
