from yogi import read

n = 0
s = 0.0
x = read(str)
while x != 'final':
    s = s + float(x)
    n = n + 1
    x = read(str)
print(s / n)
