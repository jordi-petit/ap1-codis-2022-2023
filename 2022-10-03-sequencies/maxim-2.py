from yogi import tokens, read

m = read(int)
for x in tokens(int):
    if x > m:
        m = x
print(m)
