from turtle import*
colormode(1.0)
bgcolor(0,0,0)

def color(i):
    if i%4==0: return 1,0.81,0.2
    if i%4==1: return 1,0.71,0.1
    if i%4==2: return 1,0.76,0
    return 0.9,0.71,0.1 #devuelve uno de cuatro tonos de dorado


def planta(a,b,y):
    if a>=2:
        for i in range(0,4):
            pencolor(color(i))
            antifib(a,b,60)
            right(180)
            antifib(a,b,-60)
            right(180)
            forward(y/6)
        backward(y*4/6)
        planta(b,a-b,y/1.4)

def antifib(a,b, an):
    if a>=2: #cuando a=2 estoy en el principio de la serie
        circle (b, an)
        antifib(b,a-b,an)
        circle(b, -an) #vuelve a la posición sin necesitar recordarla

def circulos(b):
    for i in range(0,10):
        seth(0)
        circle(b/20, 540)

def lagrimas(b):
    for i in range(0,2):
        seth(45+180*i)
        circle(b,90)
    seth(90)

x=int(input("¿Cúantas interaciones?"))#en la imagen, hay 13
y=float((75/1.6**13)*(1.6**x))
a, b=2, 2 #sera el primer digito de la serie de fibonacci que uso para hacer las espirales
ht()
speed(0)
for i in range(1, x): #como comienzo por la espiral más grande, calculo cual sera el último termmino
    a+=b
    b=a-b
penup()
goto(0,-a*2/3) #para que la figura entre en pantalla, comienzo moviendome abajo
pendown()
for i in range(0, x):
    pencolor(color(i))
    lagrimas(b/1.5+y/2)
    planta(a,b,y)
    circulos(b/1.5+y/2)
    b=a-b
    a=-b+a #retrocedo al paso anterior de la serie
    y=y/1.6
done()
