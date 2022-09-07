# programa que suma un segon a una hora del dia

from yogi import read

# lectura
h = read(int)
m = read(int)
s = read(int)

# sumar un segon
s = s + 1
if s == 60:
    s = 0
    m = m + 1
    if m == 60:
        m = 0
        h = h + 1
        if h == 24:
            h = 0

# escriptura
print(h, m, s)
