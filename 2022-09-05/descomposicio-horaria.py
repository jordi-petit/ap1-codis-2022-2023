# descomposició horària

from yogi import read

n = read(int)

h = n // (60 * 60)
m = (n % (60 * 60)) // 60
s = n % 60

print(h, m, s)
