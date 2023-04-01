from tkinter import *
from tkinter import messagebox
import mysql.connector as c
from PIL import Image, ImageTk
import pyscreenshot


mydb = c.connect(host='localhost',
                 user='root',
                 password='123456',
                 database='project_01')
mycursor = mydb.cursor()

class StatusFile:
    def __init__(self, root):

        self.root = root
        self.findId = StringVar()
        self.root.geometry("1500x1000")
        self.root.title("Status/Reporting")
        self.root.config(bg="#53868B")
        self.logo = PhotoImage(file='logo.png')
        self.manlogo = PhotoImage(file='gpmlogo.png')
        self.Searchicon = PhotoImage(file="search.png")



        title = Label(self.root, text="Check Status of Smart Attendance System", font=("times new roman", 40), bg='#053246',
                      fg='white').place(x=0, y=0, relwidth=1)
        self.Newhomeframe = Frame(self.root, width=1000, height=600, bd=10, bg="#053246", border=5, highlightthickness=2,
                          highlightbackground="white").place(x=300, y=150)
        # homeframedesign = Frame(root, width=1000, height=480, bd=10, bg="#053246", border=5, highlightthickness=2,
        #                         highlightbackground="white").place(x=300, y=280)
        # lb1 = Label(homeframe, text="Enter Student Id:", font=("times new roman", 20), bg="#053246", fg="white").place(
        #     x=430, y=200)
        # search = Button(homeframe, text="Search", image=self.Searchicon, bg="#053246", highlightbackground="green",
        #                 ).place(x=1050, y=200)
        # searchentry = Entry(homeframe, textvariable=self.findId, width=25, font=("times new roman", 20), bd=10).place(
        #     x=650, y=200)
        # collagelogo = Label(homeframe, text="", image=self.manlogo, bg='#053246').place(x=600, y=300)

        # create_id = Button(homeframe, width=20, text="Create Id card", font="kokila 15 bold", height=8, bd=10).place(
        #     x=1010, y=170)
        #
        genTotalCount= Button(self.root, text="Total No.of Card",command=self.totalNoOfCardGenerate, font="kokila 15 bold", width=20, height=2, bd=10).place(
            x=330, y=170)
        blockTotalCount = Button(self.root, width=20, text="Total No.of Block Card",command=self.totalNoOfCardBlock, font="kokila 15 bold", height=2,
                              bd=10).place(
            x=670, y=170)
        # totalcountlbl=Label(homeframe,text="Total No.of\nCard Gererated\nfrom System:",font="kokila 15 bold",width=20, height=8, bd=10).place(x=330,y=250)
        # blockcountlbl = Label(homeframe, text="Total No.of Block Card:", font="kokila 15 bold", width=20, height=8, bd=10).place(x=670,
        #                                                                                                          y=250)
        Blockcard = Button(self.root, width=20, text="Home", font="kokila 15 bold", height=2, bd=10).place(
            x=1010, y=170)
    def totalNoOfCardGenerate(self):
        self.queryCount = "Select(Student_ID) from studentrecord"
        mycursor.execute(self.queryCount)
        self.countList=mycursor.fetchall()
        self.count=len(self.countList)
        self.stringval=str(self.count)
        print(self.count)
        totalcountlbl=Label(self.root,text="Total No.of\nCard Gererated\nfrom System:"+self.stringval,font="kokila 25 bold",width=12, height=8, borderwidth=10).place(x=330,y=250)

    def totalNoOfCardBlock(self):
        self.queryCount = "Select count(*) from studentrecord where Block_Status=1 "
        self.mydata=mycursor.execute(self.queryCount)
        self.countList=mycursor.fetchall()
        self.count=len(self.countList)
        self.stringval=str(self.count-1)

        blockcountlbl = Label(self.root, text="Total No.of\nBlock Card:"+self.stringval, font="kokila 25 bold", width=12, height=8,
                              highlightthickness=10).place(x=670,
                                           y=250)


# root = Tk()
# obj = StatusFile(root)
# root.mainloop()