from yogi import scan

n = 0
s = 0.0
x = scan(float)
while x is not None:
    s = s + x
    n = n + 1
    x = scan(float)
print(s / n)
