from yogi import tokens

gats = 0
for paraula in tokens(str):
    if paraula == 'gat' or paraula == 'gata':
        gats = gats + 1
print(gats)
