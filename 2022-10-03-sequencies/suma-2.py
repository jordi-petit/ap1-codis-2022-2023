from yogi import scan

s = 0
x = scan(int)
while x is not None:
    s = s + x
    x = scan(int)
print(s)
