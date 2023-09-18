from tkinter import *
###create a Tk object
myroot = Tk()
###create a button within the object
###create spacing around the text inside the button
myb1 = Button(myroot, text="all the way across", highlightthickness=10)
#use padding to create space around the object in the window
myb1.grid(row = 1, column = 1, padx = 10, pady = 10)
###disable resizing
###myroot.resizable(width=False, height=False)
myroot.resizable(width=True, height=False)
###create the window from the tk object
myroot.mainloop()
