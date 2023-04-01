from tkinter import *
from tkinter.ttk import Combobox

root=Tk()
admin=StringVar()
root.geometry("500x500")
id=Combobox(root,values=['Admin','User'],textvariable=admin,state='',width=60).place(x=20,y=40)
a=admin.get()
print(a)


root.mainloop()