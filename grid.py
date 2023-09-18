from tkinter import *
myroot = Tk()

#create a button to occupy
# the 4th column on the beginning row
mybtn_col = Button(myroot, text="It is Column No. 4")
mybtn_col.grid(row=0, column=4)
#Create a button which will
# occupy four columns in width,
#Hence a columnspan of 4
mybtn_colspan = Button(myroot, text="The columnspan is of 4")
mybtn_colspan.grid(row=1,columnspan=4)
#This button will have 5
# pixels of padding on its
# outside on x axis (left/right)
mybtn_paddingx = Button(myroot, text="padx of 5 from outside widget border")
mybtn_paddingx.grid(row=2, padx=5)
#This button will have 5
# pixels of padding
# above and below it.
mybtn_paddingy = Button(myroot, text="pady of 5 from outside widget border")
mybtn_paddingy.grid(row=3,pady=5)
#this will have 5 pixels
# of padding on the
# left and right inside
mybtn_ipaddingx = Button(myroot, text="ipadx of 5 from inside widget border")
mybtn_ipaddingx.grid(row=4,ipadx=5)
#This widget will be
# padded on the top and
# bottom by 5 pixels
mybtn_ipaddingy = Button(myroot, text="ipady of 5 from inside widget border")
mybtn_ipaddingy.grid(row=5,ipady=5)
#this button will occupy
# the entirety of row 7
mybtn_row = Button(myroot, text="It is row No. 7")
mybtn_row.grid(row=7)
#this button will take
# space in three rows
mybtn_rowspan = Button(myroot, text="It is rowspan of 3")
mybtn_rowspan.grid(row=8, rowspan=3)
#This button will be anchored
# to the northwest corner
mybtn_sticky = Button(myroot, text="Hey ! I am at North-West")
mybtn_sticky.grid(sticky=NW)

myroot.mainloop()