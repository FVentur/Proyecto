from time import sleep
from tkinter import *
import random
import winsound

lista=[]

pc=[1100, 1400, 1800, 1600]

def unsort(aux):
    pcdesordenada=[]
    for x in range(len(aux)):
        azar=random.choice(aux)
        pcdesordenada.append(azar)
    return pcdesordenada
def botn1():
    rango=1100
    aux= True
    sonido(rango, aux)

def botn2():
    rango=1400
    aux= True
    sonido(rango, aux)

def botn3():
    rango=1600
    aux= True
    sonido(rango, aux)

def botn4():
    rango=1800
    aux= True
    sonido(rango, aux)

def sonido(aux, boolean):
    global pcdesordenada, lista, pc, var
    winsound.Beep(aux,300)
    if boolean:
        lista.append(aux)
        comparacion(pcdesordenada, lista, pc, var)
def Ejecutar(lis):
    aux = False
    for numero in (lis):
        sonido(numero, aux)

def comparacion(lisdes, li, pc, var):
    cont = 0
    for item,item2 in zip(lisdes, li):
        if item.__eq__(item2):
            cont += 1
        else:
            li.clear()
            var.set(0)
            break
    if cont.__ge__(len(lisdes)):
        var.set() += var.set(1)
        aux = random.choice(pc)
        lisdes.append(aux)
        li.clear()

pcdesordenada = unsort(pc)


Ventana=Tk()
Ventana.geometry("700x500")
Ventana.config(bg='black')
Ejecutar(pcdesordenada)

var = IntVar()
label = Label(Ventana, textvariable=var).grid(row=0, column=1)


boton = Button(Ventana, text="iniciar sonido", command=botn1, height = 15, width = 35, bg='red').grid(row=1, column=1)
boton2 = Button(Ventana, text="iniciar sonido", command=botn2, height = 15, width = 35, bg='green').grid(row=1, column=2)
boton3 = Button(Ventana, text="iniciar sonido", command=botn3, height = 15, width = 35, bg='yellow').grid(row=2, column=1)
boton4 = Button(Ventana, text="iniciar sonido", command=botn4, height = 15, width = 35, bg='blue').grid(row=2, column=2)

boton5 = Button(Ventana, text="ejecutar sonido", command=lambda: Ejecutar(pcdesordenada), bg='orange').grid(row=0, column=0)
Ventana.mainloop()

