# programa que calcula el màxim de dos nombres

from yogi import read

x = read(int)
y = read(int)
if x > y:
    m = x
else:
    m = y
print(m)
