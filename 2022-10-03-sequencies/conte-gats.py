from yogi import scan

hi_ha_gats = False
paraula = scan(str)
while paraula is not None and not hi_ha_gats:
    if paraula == 'gat':
        hi_ha_gats = True
    else:
        paraula = scan(str)
print(hi_ha_gats)
