import re
from tkinter import *
from tkinter import messagebox
root=Tk()
varemailid = StringVar()
# emailid=varemailid.get()
# print(emailid)
def valid():
    emailregex =r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Z|a-z]{2,}\b'
    mobileregex=r'\d{10}'
    nameregex=r'^([a-z]+)([a-z]+)*([a-z]+)*$'
    idregex='\d{10}'
    if (re.fullmatch(nameregex, varemailid.get())):
        messagebox.showinfo("Info","Valid input")
        # print(emailid)

    else:
        messagebox.showerror("Error","Invalid input")
        # print(emailid)

root.geometry("500x500")
emial=Entry(root,width=20,bd=5,textvariable=varemailid).place(x=20,y=200)
check=Button(root,text="Check",bg="blue",command=valid).place(x=20,y=300)
root.mainloop()

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)