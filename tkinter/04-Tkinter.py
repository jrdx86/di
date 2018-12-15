from tkinter import *

root  = Tk()
root.title("Cuenta Genomas")

miFrame=Frame(root, width =80, height = 30)
miFrame.pack()

txt = Text(root,width =25, height = 8)
txt.pack()

Boton = Button(root,text="Count",command=lambda:retrieve_input())
Boton.pack()

def retrieve_input():
    """Accede al string de txt.
    Cuenta las letras que buscamos en el text y cuenta el numero de repeticiones
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

label0 = Label(root, text="Num As:")
label0.pack(side="left")
label1 = Label(root, textvariable = A)
label1.pack(side="left")

label2 = Label(root, text="Num Ts:")
label2.pack(side="left")
label4 = Label(root, textvariable =T)
label4.pack(side="left")

label3 = Label(root, text="Num Cs:")
label3.pack(side="left")
label5 = Label(root, textvariable = C)
label5.pack(side="left")

label4 = Label(root, text="Num Gs:")
label4.pack(side="left")
label6 = Label(root, textvariable = G)
label6.pack(side="left")

root.mainloop()