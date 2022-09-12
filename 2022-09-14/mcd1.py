# programa per calcular el màxim comú divisor de dos naturals
# versió senzilleta (i lenta)

import yogi

a = yogi.read(int)
b = yogi.read(int)

if a < b:
    d = a
else:
    d = b
while a % d != 0 or b % d != 0:
    d = d - 1
print(f'mcd({a},{b}) = {d}')
