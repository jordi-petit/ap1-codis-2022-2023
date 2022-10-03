#número del revés
from yogi import read


n = read(int) #llegim el número
a = str(n)  #convertim la variable a string

b= a[::-1] #funció pròpia de python per reversear un string
print(b)


for i in range(len(a)-1): #repetim el bucle tantes vegades com dígits - 1.
    r = n%10 #empram la funció del residu per obtenir el darrer nombre
    print(r, end="") #el printejam
    n = n//10 #feim que n prengui el valor de n - el darrer dígit
print(n) #imprimim el darrer dígit (que és el primer digit del nombre
# inicial per tal que no doni presentation error degut a l'end = "")
