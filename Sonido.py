from time import sleep
from pyo import *
from tkinter import *
def sonido():
    server = Server().boot()
    server.start()
    sine = Sine(300.63, mul=0.1).out()
    sleep(3)
    server.stop()
Ventana=Tk()
Ventana.geometry("300x300")
boton = Button(Ventana, text="ejecutar sonido", command=sonido).grid()
Ventana.mainloop()
