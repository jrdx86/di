#!/bin/python3

import tkinter

window=tkinter.Tk()
label = tkinter.Label(window, text="This is our label.")
label.pack()
label.config(text="Second label.")
window.mainloop()