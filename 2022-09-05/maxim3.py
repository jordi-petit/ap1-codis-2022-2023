# programa que calcula el màxim de tres nombres

from yogi import read

x = read(int)
y = read(int)
z = read(int)
if x >= y and x >= z:
    m = x
elif y >= x and y >= z:
    m = y
else:
    m = z
print(m)

# també hem vist com es pot fer amb condicionals aniuats
