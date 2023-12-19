
from turtle import * 
from math import *
enota = 40.0 #enota je 40pik na sliki

def os(): # nariše os
    for i in range(-5,6):
        lt(90)
        fd(10)
        write(i)
        bk(10)
        rt(90)
        fd(enota)
def ks(): #nariše koordinatni sistem
    reset()
    bk(5*enota)
    os()
    bk(6*enota)
    lt(90)
    bk(5*enota)
    os()
    home()

def graf(fun):
    f = lambda x: eval(fun)  #definicija anonimne funkcije iz niza  
    tracer(100) #hitreje
    ks()
    color("red")
    pensize(3)
    pu()
    goto(-5*enota,f(-5)*enota)
    pd()
    tracer(1)
    for i in range(-200,200,2):
        try:
            goto(i,f(i/enota)*enota)
        except:
            pass
    mainloop()

graf('(x**2 - 3)/(x-1)')
