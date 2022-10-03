from yogi import *

repetits = 0
par1 = scan(str)
if par1 is not None:
    par2 = scan(str)
    while par2 is not None:
        if par1 == par2:
            repetits = repetits + 1
        par1, par2 = par2, scan(str)
print(repetits)
