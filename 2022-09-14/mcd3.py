# programa per calcular el màxim comú divisor de dos naturals
# amb l'algorisme d'Euclides (versió amb mòduls)

import yogi

a = yogi.read(int)
b = yogi.read(int)

while b != 0:
    r = a % b
    a = b
    b = r

print(a)
