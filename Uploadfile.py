from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import mysql.connector as c
import os, shutil


def uploadPhoto():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                          filetypes=(("JPG file", "*.jpg"), \
                                                     ("PNG file", "*.png"), ("All files", "*.*")))
    img = Image.open(fln)
    img.thumbnail((350, 350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img


root=Tk()
root.geometry("500x500")
frame=Frame(root).pack(side=BOTTOM,padx=15,pady=15)
lbl=Label(root)
lbl.pack()
btn1=Button(root,text="select images",command=uploadPhoto).pack(side=tk.LEFT)
root.mainloop()
