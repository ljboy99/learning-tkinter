import tkinter
from tkinter import *

myroot = Tk()

#myroot.geometry("60x60")
button0 = Button(text="tiny", fg='LightBlue', bg='Black')
button0.grid(row=0,column=0)
button1 = Button(text="Hello", fg='red', activebackground='gray', activeforeground='red')
button1.grid(row=0, column = 1)
button2 = Button(text="Button")
button2.grid(row=0,column=2)

myroot.mainloop()