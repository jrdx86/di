#! /usr/bin/python3
import tkinter

window = tkinter.Tk()
button = tkinter.Button(window, text='Adios',
    font=('Courier', 14, 'bold italic'),command=window.quit)#Cuando pulsamos este boton con el comando quit cerramos window
button.pack()
window.mainloop()