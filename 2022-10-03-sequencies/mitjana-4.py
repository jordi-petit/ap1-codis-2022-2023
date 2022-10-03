from yogi import tokens

n = 0
s = 0.0
for x in tokens(float):
    s = s + x
    n = n + 1
print(s / n)
