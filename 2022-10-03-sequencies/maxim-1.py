from yogi import scan, read

m = read(int)
x = scan(int)
while x is not None:
    if x > m:
        m = x
    x = scan(int)
print(m)
