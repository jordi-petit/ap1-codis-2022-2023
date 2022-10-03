from yogi import read

n = read(int)
s = 0.0
for i in range(n):
    x = read(float)
    s = s + x
print(s / n)
