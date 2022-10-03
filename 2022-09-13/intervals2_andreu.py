from yogi import read

a0 = read(int)
a1 = read(int)
b0 = read(int)
b1 = read(int)

#Comprovem si els dos intervals són iguals
if a0 == b0 and a1 == b1:
    print("=")
#Sinó, mirem si el 1r interval està contingut en el 2n
#Perquè això es doni, cal que a0 sigui més petit que b0, però que a1 sigui més gran que b1
#Afegim l'igual perquè el 1r interval pot començar just on começa el 2n, o acabar just on acaba, i encara així estar contingut
elif a0 >= b0 and a1 <= b1:
    print("1")
#Apliquem el mateix en el cas contrari: el 2n interval està contingut en el 1r
elif a0 <= b0 and a1 >= b1:
    print("2")
#Si no es compleix cap d'aquestes condicions, cap interval està contingut en l'altre
else:
    print("?")