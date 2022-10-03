from yogi import tokens

s = 0
for x in tokens(int):
    s = s + x
print(s)
