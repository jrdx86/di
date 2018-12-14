import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text='Adios',
font=('Courier', 14, 'bold italic'),command=window.quit)
button.pack()
window.mainloop()