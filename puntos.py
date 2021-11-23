from tkinter import *
from tkinter import ttk
class Puntaje():
    def __init__(self,Master):
        self.Master=Master
        self.marcador = IntVar()
    def funcion(self):
        self.label = Label(self.Master, textvariable=self.marcador, font=("Comic Sans", 20), bg='black', fg="white").grid(row=0, column=2)
