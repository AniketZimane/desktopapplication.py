from tkinter import PhotoImage
import tkinter
from FindIdCard import *
from OpenCVModule import *
from StatusFile import *
import tkinter as tk

# from StatusFile import *
import cv2
from tkinter import *
from tkinter import messagebox
import mysql.connector as c
from PIL import Image, ImageTk
import pyscreenshot

from tkinter import *
from tkinter import messagebox
import mysql.connector as c
from PIL import Image, ImageTk
import pyscreenshot

from ORcodeGUI import *

mydb = c.connect(host='localhost',
                 user='root',
                 password='123456',
                 database='project_01')
mycursor = mydb.cursor()

# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

# setting root window:
root = tk.Tk()
root.title("DashBoard")
root.config(bg="#053246")
root.geometry("1920x1080")

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="theeline.png")
closeIcon = PhotoImage(file="closeicon.png")
searchIcon = PhotoImage(file="searchicon.png")
scanimg = PhotoImage(file="card.png")
checkStatusicon = PhotoImage(file="status.png")
createidicon = PhotoImage(file="createid.png")
findusericon = PhotoImage(file="findstudent.png")
blockicon = PhotoImage(file="blockcard.png")
leaveicon = PhotoImage(file="leave.png")
logo = PhotoImage(file='logo.png')


#
def FindIdCardUser():
    print("Function call")
    root1 = Tk()
    obj2 = FindIdCard(root1)
    root1.mainloop()


#     # root.destroy()

# setting switch function:
middleFrame = tk.Frame(root, width=1000, height=600, bd=10, bg="#053246", border=5, highlightthickness=2,
                       highlightbackground="white").place(x=300, y=150)
lbl = tk.Label(middleFrame, text="Welcome to Smart\n Attendance Management System", font="kokila 40 bold", bg="#053246",
               fg="white").place(x=380, y=350)


def profilecontent():
    pass

def GenerateId():
    root=Tk()
    obj=ORcodeGUI(root)
    return obj

def statusFile():
    root = Tk()
    obj = StatusFile(root)
    root.mainloop()
    # root.destroy()


def scanCard():
    scancard()


# root.destroy()

homeframe = tk.Frame(root, width=1000, height=600, bd=10, bg="#053246", border=5, highlightthickness=2,
                     highlightbackground="white").place(x=300, y=150)
tk.Button(homeframe, text="", image=scanimg, command=scanCard, font="kokila 15 bold", padx=200, pady=200,
          borderwidth=10).place(x=330,
                                y=170)
tk.Button(homeframe, text="", image=checkStatusicon, command=statusFile, font="kokila 15 bold", padx=200, pady=200,
          borderwidth=10,
          ).place(x=670, y=170)
tk.Button(homeframe, text="", image=createidicon,command=GenerateId, font="kokila 15 bold", padx=200, pady=200, borderwidth=10,
          ).place(x=1010,
                  y=170)

tk.Button(homeframe, text="", image=findusericon, command=FindIdCardUser, font="kokila 15 bold", padx=200, pady=200,
          borderwidth=10, ).place(x=330,
                                  y=460)
tk.Button(homeframe, text="", image=blockicon, font="kokila 15 bold", padx=200, pady=200, borderwidth=10,
          ).place(x=670,
                  y=460)
tk.Button(homeframe, text="", image=leaveicon, font="kokila 15 bold", padx=200, pady=200, borderwidth=10,
          ).place(x=1010,
                  y=460)


def homeContent():
    pass


def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:

        homeLabel.config(bg="white")
        topFrame.config(bg="white")
        root.config(bg="#053246")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        # brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg="#053246")
        topFrame.config(bg="#053246")
        root.config(bg="#053246")

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True


# top Navigation bar:
topFrame = tk.Frame(root, bg="white")
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="Government Polytechnic Malvan", font="Bahnschrift 15", bg="white", fg="black",
                     height=2, padx=20)
homeLabel.pack(side="right")

# Navbar button 3line:
navbarBtn = tk.Button(topFrame, image=navIcon, bg="white", activebackground="green", bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="#53868B", height=1000, width=300)
navRoot.place(x=-300, y=0)
# X sign panel
tk.Label(navRoot, font="Bahnschrift 15", bg="#053246", fg="white", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Profile", "Settings", "Help", "About", "Feedback"]
# Navbar Option Buttons:
# for i in range(5):

profileicon = PhotoImage(file="profile1.png")
settingicon = PhotoImage(file="setting.png")
helpicon = PhotoImage(file="help.png")
# abouticon=PhotoImage(file="")
feedbackicon = PhotoImage(file="feedback.png")
logouticon = PhotoImage(file="logout.png")

#     tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"], activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
tk.Button(navRoot, text="Profile", font="BahnschriftLight 15", bg="#53868B", fg="white"
          , activebackground="#53868B", activeforeground="green", bd=0, command=profilecontent).place(x=40, y=80)
tk.Button(navRoot, text="Settings", font="BahnschriftLight 15", bg="#53868B", fg="white",
          activebackground="#53868B", activeforeground="green", bd=0, command=homeContent).place(x=40, y=120)
tk.Button(navRoot, text="Help", font="BahnschriftLight 15", bg="#53868B", fg="white",
          activebackground="#53868B", activeforeground="green", bd=0).place(x=40, y=160)
tk.Button(navRoot, text="About", font="BahnschriftLight 15", bg="#53868B", fg="white",
          activebackground="#53868B", activeforeground="green", bd=0).place(x=40, y=200)
tk.Button(navRoot, text="Feedback", font="BahnschriftLight 15", bg="#53868B", fg="white",
          activebackground="#53868B", activeforeground="green", bd=0).place(x=40, y=240)

tk.Button(navRoot, text="Log out", font="BahnschriftLight 15", bg="#53868B", fg="white",
          activebackground="gray17", activeforeground="green", bd=0).place(x=40, y=280)

tk.Label(navRoot, bg="gray17", fg=color["orange"],
         image=profileicon, activebackground="gray17", activeforeground="green", bd=0).place(x=10, y=80)
tk.Label(navRoot, bg="gray17", fg=color["orange"],
         image=settingicon, activebackground="gray17", activeforeground="green", bd=0).place(x=10, y=120)
tk.Label(navRoot, bg="gray17", fg=color["orange"],
         image=helpicon, activebackground="gray17", activeforeground="green", bd=0).place(x=10, y=160)
tk.Label(navRoot, bg="gray17", fg=color["orange"],
         image=feedbackicon, activebackground="gray17", activeforeground="green", bd=0).place(x=10, y=200)
tk.Label(navRoot, bg="gray17", fg=color["orange"],
         image=profileicon, activebackground="gray17", activeforeground="green", bd=0).place(x=10, y=240)

tk.Label(navRoot, text="Log out", bg="gray17", fg=color["orange"],
         image=logouticon, activebackground="gray17", activeforeground="green", bd=0).place(x=10, y=280)
# y += 440
# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg="white", activebackground="green", bd=0, command=switch)
closeBtn.place(x=250, y=10)

# window in mainloop:
root.mainloop()
