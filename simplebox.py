from tkinter import *
###create a Tk object
myroot = Tk()
###create a widget within the object
###the bd stands for borderwidth
myl1 = Label(myroot, text="Label 1", bd=8, relief='groove')
myl1.pack()
###disable resizing
###myroot.resizable(width=False, height=False)
myroot.resizable(width=True, height=False)
###create the window from the tk object
myroot.mainloop()
