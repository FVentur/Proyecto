from time import sleep
from pyo import *
from tkinter import *
from random import randint

lista=[]

def random():
    rango=randint(100,1000)
    aux = True
    sonido(rango, aux)

def sonido(aux, boolean):
    global lista
    server = Server().boot()
    server.start()
    sine = Sine(aux, mul=4.2).out()
    sleep(1)

    if boolean:

        lista.append(aux)
        print(lista)
    server.stop()
def Ejecutar(lis):
    aux = False
    for numero in (lis):
        sonido(numero, aux)


Ventana=Tk()
Ventana.geometry("300x300")
boton = Button(Ventana, text="iniciar sonido", command=random, height = 20, width = 20, bg='red').grid(row=0, column=0)
boton2 = Button(Ventana, text="ejecutar sonido", command=lambda: Ejecutar(lista), height = 20, width = 20, bg='green').grid(row=0, column=1)
Ventana.mainloop()
