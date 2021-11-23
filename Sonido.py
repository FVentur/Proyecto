from time import sleep
from tkinter import *
from puntos import Puntaje
from Frame import frame
import random
import winsound

class App():
    def unsort(self,aux):
        pcdesordenada=[]
        for x in range(len(aux)):
            azar=random.choice(aux)
            pcdesordenada.append(azar)
        return pcdesordenada
    def botn1(self):
        rango=1100
        aux= True
        self.sonido(rango, aux)


    def botn2(self):
        rango=1400
        aux= True
        self.sonido(rango, aux)


    def botn3(self):
        rango=1600
        aux= True
        self.sonido(rango, aux)


    def botn4(self):
        rango=1800
        aux=True
        self.sonido(rango, aux)


    def sonido(self,aux, boolean):
        self.pcdesordenada
        self.lista
        self.pc
        winsound.Beep(aux,300)
        if boolean:
            self.lista.append(aux)
            self.comparacion(self.pcdesordenada, self.lista, self.pc)
    def Ejecutar(self,lis):
        aux = False
        for numero in (lis):
            self.sonido(numero, aux)

    def comparacion(self,lisdes, li, pc):
        cont = 0
        for item,item2 in zip(lisdes, li):
            if item.__eq__(item2):
                cont += 1
            else:
                li.clear()
                self.Puntos.marcador.set(0)
                for i in range (len(lisdes)):
                    cont = 0
                    if i.__gt__(0):
                        lisdes.pop(1)
                break
            if cont.__ge__(len(lisdes)):
                self.Puntos.marcador.set(self.Puntos.marcador.get() + 1)
                aux = random.choice(pc)
                lisdes.append(aux)
                li.clear()

    def sonido_teclado(self,event):
        if event.keysym.__eq__('Up'):
            self.botn4()
        if event.keysym.__eq__('Down'):
            self.botn1()
        if event.keysym.__eq__('Left'):
            self.botn3()
        if event.keysym.__eq__('Right'):
            self.botn2()
        if event.keysym.__eq__('space'):
            self.Ejecutar(self.pcdesordenada)

    def __init__(self,pestania):
        self.lista = []
        self.otralista = []
        self.puntaje = 0
        self.pestania=pestania
        self.Puntos = Puntaje(self.pestania.getFrame())
        self.Puntos.funcion()
        self.pc = [1100, 1400, 1800, 1600]
        self.pcdesordenada = self.unsort(self.pc)




