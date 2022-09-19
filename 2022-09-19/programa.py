from yogi import read

x = read(int)
if x % 2 == 0:
    print('hola' + x)  # error!
else:
    print('adeu')
