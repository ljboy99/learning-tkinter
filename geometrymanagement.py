from tkinter import *
myroot = Tk()
myroot.geometry('300x300')
myb1 = Button(myroot, text='P', fg='Red', bg='LightGreen')
myb1.pack(fill = None)
#Fill = X will fill the x axis with the object
myb2 = Button(myroot, text='Y', fg='Red', bg='LightGreen')
myb2.pack(fill = X, padx = 10, pady = 10)
#side = left will push that object to the left
#fill = y will spread that object across the y axis
myb3 = Button(myroot, text='T', fg='Red', bg='LightGreen')
myb3.pack(side=LEFT, fill=Y, padx=10, pady=10)
myb3 = Button(myroot, text='H', fg='Red', bg='LightGreen')
myb3.pack(side=TOP, fill=X, padx=10, pady=10)
myb4 = Button(myroot, text='O', fg='Red', bg='LightGreen')
myb4.pack(side=BOTTOM, fill=X, padx=10, pady=10)
#by saying fill = BOTH and expand = 1, we let the object
#fill up the empty space surrounding it.
myb5 = Button(myroot, text='N', fg='Red', bg='LightGreen')
myb5.pack(side=RIGHT, fill=BOTH, expand = 1, padx=10, pady=10)

myroot.mainloop()