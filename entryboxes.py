from tkinter import *
myroot = Tk()
###create text entry box
mye1=Entry(myroot, bg='LightGreen', highlightthickness=10, highlightbackground="red", highlightcolor='Yellow')
mye1.pack(padx=5, pady=5)
###When you select text, you can change the colors
###of both the selection and the text
mye2 = Entry(myroot, selectbackground= 'Green', selectforeground= 'Red')
mye2.pack()
### .focus() will make one of the text boxes
### active when the script starts
mye1.focus()
myroot.mainloop()