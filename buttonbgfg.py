from tkinter import *
myroot = Tk()
###Create a button where when clicked, it turns red
###You can also do this with activeforeground / fg
myb1 = Button(myroot, activebackground = "#ff0000",
              #when not clicked, button is green
              bg = '#00ff00', text = 'python')
myb1.pack()
myb2 = Button(myroot, activeforeground='#ff0000', fg = '#0000ff', text= 'python')
myb2.pack(pady=10)
myroot.mainloop()