#! /usr/bin/python3

import tkinter
import tkinter.filedialog as dialog



class Application():
    def save(root, text):
        data = text.get( '0.0' , tkinter.END)
        filename = dialog.asksaveasfilename(
            parent=root,
            filetypes=[( 'Text' , '*.txt' )],
            title= 'Save as...' )
            
        writer = open(filename, 'w' )
        writer.write(data)
        writer.close()
    def quit(root):
        root.destroy()


window = tkinter.Tk()
text = tkinter.Text(window)
text.pack()
menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label= 'Save' ,command= lambda :Application.save(window, text))
filemenu.add_command(label= 'Quit' ,command= lambda :Application.quit(window))
menubar.add_cascade(label = 'File' , menu=filemenu)
window.config(menu=menubar)
window.mainloop()