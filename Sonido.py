from time import sleep
from tkinter import *
import random
import winsound

lista = []
otralista = []
pc = [1100, 1400, 1800, 1600]
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
    global pcdesordenada, lista, pc
    winsound.Beep(aux,300)
    if boolean:
        lista.append(aux)
        comparacion(pcdesordenada, lista, pc)
def Ejecutar(lis):
    aux = False
    for numero in (lis):
            sonido(numero, aux)
def comparacion(lisdes, li, pc):
    cont = 0
    for item,item2 in zip(lisdes, li):
        if item.__eq__(item2):
            cont += 1
        else:
            li.clear()
            puntaje.set(0)
            for i in range (len(lisdes)):
                cont = 0
                if i.__gt__(0):
                    lisdes.pop(1)
            break
    if cont.__ge__(len(lisdes)):
        puntaje.set(int(puntaje.get())+1)
        aux = random.choice(pc)
        lisdes.append(aux)
        li.clear()
def sonido_teclado(event):
    if event.keysym.__eq__('Up'):
        botn4()
    if event.keysym.__eq__('Down'):
        botn1()
    if event.keysym.__eq__('Left'):
        botn3()
    if event.keysym.__eq__('Right'):
        botn2()
    if event.keysym.__eq__('space'):
        Ejecutar(pcdesordenada)


pcdesordenada = unsort(pc)


Ventana=Tk()
Ventana.geometry("700x520")
Ventana.config(bg='black')
canvas = Canvas(Ventana,height = 15, width = 35, bg='black')
canvas.grid()
puntaje = IntVar()
label = Label(Ventana, textvariable=puntaje, font=("Comic Sans", 20), bg='black', fg="white").grid(row=0, column=2)


canvas.bind_all('<KeyPress-Up>',sonido_teclado)
canvas.bind_all('<KeyPress-Down>',sonido_teclado)
canvas.bind_all('<KeyPress-Left>',sonido_teclado)
canvas.bind_all('<KeyPress-Right>',sonido_teclado)
canvas.bind_all('<space>',sonido_teclado)

boton = Button(Ventana, command=botn1, height = 15, width = 35, bg='red').grid(row=1, column=1)
boton2 = Button(Ventana, command=botn2, height = 15, width = 35, bg='green').grid(row=1, column=2)
boton3 = Button(Ventana, command=botn3, height = 15, width = 35, bg='yellow').grid(row=2, column=1)
boton4 = Button(Ventana, command=botn4, height = 15, width = 35, bg='blue').grid(row=2, column=2)

boton5 = Button(Ventana, text="ejecutar sonido", command=lambda: Ejecutar(pcdesordenada), bg='orange').grid(row=0, column=0)


Ventana.mainloop()

