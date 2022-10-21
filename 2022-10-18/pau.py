from turtle import *

def fractal(n: int, d: int) -> None:
    """Funció recursiva que fa un fractal brutal"""
    if n == 1:
        for _ in range(3):
            fd(d)
            lt(90)
        fd(d)
    else:
        fd(d) #reposicionació primer quadrat
        lt(90)
        fd(d)
        rt(90)
        fractal(n-1, d//2)

        rt(90) #reposicionació segon quadrat
        fd(d + d//2)
        seth(0)
        fractal(n-1, d//2)
        
        lt(90) #reposicionació tercer quadrat
        fd(d//2)
        rt(90)
        fd(d)
        fd(d//2)
        rt(90)
        fd(d//2)
        seth(0)
        fractal(n-1, d//2)

        up() #reposicionament per enllaçar la recursivitat 
        lt(90) 
        fd(d//2)
        lt(90)
        fd(d//2)
        seth(270)
        down()

def reposicionament(d: int) -> None:
    """Funció que posiciona el cursos de tal manera que el fractal estigui centrat"""
    up()
    seth(180)
    fd(d)
    lt(90)
    fd(d)
    seth(0)
    down()

def main():
    n = 4
    d = 200
    reposicionament(d//2)
    speed(0)
    fractal(n, d)
    hideturtle()
    done()

if __name__ == "__main__":
    main()
