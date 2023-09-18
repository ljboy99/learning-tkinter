from tkinter import *
###create a Tk object
myroot = Tk()
###wrap the letters
myl1 = Label(myroot, text="vertical", wraplength=2)
myl1.pack()
###Create space around a label and choose a font
myl2 = Label(myroot, text="horizontal", width=20, height= 5, font=('Verdana', 20))
myl2.pack()
###create the window from the tk object
myroot.mainloop()
