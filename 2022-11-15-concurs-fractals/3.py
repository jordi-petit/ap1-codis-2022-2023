#EL CÓDIGO GENERA LA IMAGEN PNG ADJUNTA, PERO ROTADA 90 GRADOS. CONSISTE EN UN MOTIVO QUE SE VA REPITIENDO, PERO CAMBIANDO DE SITIO EN CADA ITERACIÓN DEPENDIENDO DE SU POSICIÓN INICIAL Y FINAL.
#EL RESULTADO ES UNA ESPIRAL CON ESPIRALES MÁS PEQUEÑAS EN SU COSTADO, QUE A SU VEZ PRESENTAN OTRAS MÁS PEQUEÑAS. ESTE FRACTAL RECUERDA A UN CABALITO DE MAR.

from turtle import *
from math import *

bgcolor('#b3ffff')
def dragon(n,l)->None:
    if n==0:
        #EL COLOR VARÍA GRADUALMENTE CON LA COORDENADA EN X.
        color(255,90,int((xcor()+1050)*255/2100)) 
        
        
        lt(30)
        forward(l/sqrt(3))
        rt(120)
        forward(l/sqrt(3))
        lt(30)
        
    else:
        X1=xcor()
        Y1=ycor()
        
        dragon(n-1,l)
        
        X2=xcor()
        Y2=ycor()
        H=heading()
        X3=X2+(Y2-Y1)
        Y3=Y2-(X2-X1)
    
        penup()
        goto(X3,Y3)
        lt(90)
        pendown()
        
        dragon(n-1,l)
        
        
        penup()
        goto(X3,Y3)
        setheading(H)
        pendown()

ht()
colormode(255)
tracer(500000)
#LA HERRAMIENTA TRACER PERMITE GENERAR EL FRACTAL EN MENOS TIEMPO, MOSTRANDO 1 DE CADA 500000 FRAMES, EN ESTE CASO.
speed(0)


pensize(1.5)
setheading(30)

n=16
l=7

penup()
goto(-450,-380)
pendown()

dragon(n,l)

done()
