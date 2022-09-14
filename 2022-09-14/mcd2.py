# programa per calcular el màxim comú divisor de dos naturals
# amb l'algorisme d'Euclides (versió amb restes)

import yogi

a = yogi.read(int)
b = yogi.read(int)

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)
