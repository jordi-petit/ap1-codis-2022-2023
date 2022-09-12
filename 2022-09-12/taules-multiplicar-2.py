# programa que escriu les taules de multiplicar
# amb un bucle for i posant els números en columnes.

for i in range(11):
    print('taula del', i)
    for j in range(11):
        print(f'{i:2d} * {j:2d} = {i*j:3d}')
    print()
