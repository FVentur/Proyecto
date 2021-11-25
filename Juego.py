from Sonido import App
from puntos import Puntaje
from Frame import frame
from tkinter import *

Ventana=Tk()
Ventana.geometry("700x520")
Ventana.config(bg='black')
canvas = Canvas(Ventana,height = 15, width = 35, bg='black')
canvas.grid()
pestania=frame()
pestania.setFrame(Ventana)
app = App(pestania)
pcdesordenada = app.pcdesordenada

canvas.bind_all('<KeyPress-Up>', app.sonido_teclado)
canvas.bind_all('<KeyPress-Down>', app.sonido_teclado)
canvas.bind_all('<KeyPress-Left>',app.sonido_teclado)
canvas.bind_all('<KeyPress-Right>',app.sonido_teclado)
canvas.bind_all('<space>',app.sonido_teclado)
boton5 = Button(Ventana, text="ejecutar sonido", command=lambda:  app.Ejecutar(pcdesordenada), bg='orange').grid(row=0, column=0)

boton = Button(Ventana, command=app.botn1, height = 15, width = 35, bg='red').grid(row=1, column=1)
boton2 = Button(Ventana, command=app.botn2, height = 15, width = 35, bg='green').grid(row=1, column=2)
boton3 = Button(Ventana, command=app.botn3, height = 15, width = 35, bg='yellow').grid(row=2, column=1)
boton4 = Button(Ventana, command=app.botn4, height = 15, width = 35, bg='blue').grid(row=2, column=2)

Ventana.mainloop()