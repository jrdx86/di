#! /usr/bin/python3
from tkinter import *

root  = Tk()
root.title("Cuenta Genomas")

miFrame=Frame(root, width =300, height = 300)
miFrame.pack()

txt = Text(miFrame,width =25, height = 8)
txt.pack()

Boton = Button(miFrame,text="Count",command=lambda:retrieve_input())
Boton.pack()

def retrieve_input():
    """Accede al string de txt.
    Cuenta las letras que buscamos en el text y cuenta el numero de repeticiones
    Variables:
        A= str
        T= str
        C= str
        G= str


    """
    input = txt.get("1.0",'end-1c').upper()
    A.set(input.count(str("A"))) 
    T.set(input.count(str("T")))
    C.set(input.count(str("C")))
    G.set(input.count(str("G")))

A = IntVar()
T = IntVar()
C = IntVar()
G = IntVar()

label0 = Label(miFrame, text="Num As:")
label0.pack(side="left")
label1 = Label(miFrame, textvariable = A)
label1.pack(side="left")

label2 = Label(miFrame, text="Num Ts:")
label2.pack(side="left")
label4 = Label(miFrame, textvariable =T)
label4.pack(side="left")

label3 = Label(miFrame, text="Num Cs:")
label3.pack(side="left")
label5 = Label(miFrame, textvariable = C)
label5.pack(side="left")

label4 = Label(miFrame, text="Num Gs:")
label4.pack(side="left")
label6 = Label(miFrame, textvariable = G)
label6.pack(side="left")

root.mainloop()