from tkinter import *

root  = Tk()
root.title("Conversor Fahrenhait")

label0 = Label(root, text="Temperature in Fahrenheit: ")
label0.pack()

mEntry = Entry(root)
mEntry.pack()

def convert_to_celsius():
    """Convierte F a C
    (fahrenheit - 32) * 5 / 9
    Variables
        F = int
        L = int
    """
    F= ((int(mEntry.get())-32)*5/9)
    L.set(F)
    mEntry.insert(0,str(F))

def quit():
    root.destroy()



L = IntVar()
label1 = Label(root, textvariable = L)
label1.pack()

Boton1 = Button(root,text="Convert to Celsius",command=convert_to_celsius)
Boton1.pack()

Boton2 = Button(root,text="Quit", command=quit)
Boton2.pack()

root.mainloop()