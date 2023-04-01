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

class FindIdCard:
    def __init__(self, root):
        self.root = root
        self.findId = StringVar()
        self.root.geometry("1500x1000")
        self.root.title("QR code generator")
        self.root.config(bg="#53868B")
        self.logo = PhotoImage(file='logo.png')
        self.manlogo = PhotoImage(file='gpmlogo.png')
        self.Searchicon = PhotoImage(file='search.png')

        self.title = Label(self.root, text="Find Id card", font=("times new roman", 40), bg='#053246',
                      fg='white').place(x=0, y=0, relwidth=1)
        self.homeframe = Frame(self.root, width=1000, height=600, bd=10, bg="#053246", border=5, highlightthickness=2,
                          highlightbackground="white").place(x=300, y=150)
        self.homeframedesign = Frame(self.root, width=1000, height=480, bd=10, bg="#053246", border=5, highlightthickness=2,
                                highlightbackground="white").place(x=300, y=280)
        self.lb1 = Label(self.root, text="Enter Student Id:", font=("times new roman", 20), bg="#053246", fg="white").place(
            x=430, y=200)
        self.searchentry = Entry(self.root, textvariable=self.findId, width=25, font=("times new roman", 20),
                                 bd=10).place(
            x=650, y=200)
        self.search = Button(self.root, text="Search",image=self.Searchicon, bg="#053246", highlightbackground="green",
                        command=self.FindMYId).place(x=1050, y=200)

        self.collagelogo = Label(self.root, text="", image=self.manlogo, bg='#053246').place(x=600, y=300)

    def ProfileDisplay(self):
        self.profile = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.profile.place(x=300, y=400, width=200, height=200)

    def saveIdCard(self):
        self.image = pyscreenshot.grab(bbox=(655, 400, 1490, 900))  # x1,x2,y1,y2 y1=width y2=height
        # self.image.show()
        self.id=self.findId.get()
        self.image.save('Identycard/img{0}.png'.format(str(self.id)))
        messagebox.showinfo("info","Your card save successfuly........")
        # 'RetriveProfileImages/profile_{0}.png'.format(str(self.findId.get())))

    def FindMYId(self):
        selectQuery = "select Name,Department,Photo,QRImage from studentrecord where Student_ID=%s"
        self.Select_val = [(self.findId.get())]
        print(self.Select_val)
        count = mycursor.execute(selectQuery, self.Select_val)
        result = mycursor.fetchone()
        if self.findId.get() == "" or not result:
            messagebox.showinfo("info", "Enter valid student id....")
        else:
            if result:
                mydataList = list(result)
                self.qr_main_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
                self.qr_main_frame.place(x=500, y=300, width=650, height=390)
                self.qr_main_frame.config(bg="orange")
                self.qr_second_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
                self.qr_second_frame.place(x=840, y=345, width=300, height=110)
                self.qr_second_frame.config(bg="pink")
                self.print_dept = mydataList[1] + "\nEngineering"
                lbl_dept = Label(self.qr_main_frame, text=self.print_dept, bg="orange", font=("times new roman", 20),
                                 fg="black")
                lbl_dept.place(x=50, y=220, width=280, height=70)
                self.print_name = mydataList[0]
                lbl_name_card = Label(self.qr_second_frame, text=self.print_name, bg="pink",
                                      font=("times new roman", 15), fg="black")
                lbl_name_card.place(x=60, y=10, width=160, height=20)
                self.print_code = self.findId.get()
                lbl_en_no_card = Label(self.qr_second_frame, text=self.print_code, bg="pink",
                                       font=("times new roman", 15), fg="black")
                lbl_en_no_card.place(x=150, y=40, width=130, height=20)

                qr_title = Label(self.qr_main_frame, text="Students IdentyCard", font=("goudy old style", 20),
                                 bg='#043256',
                                 fg='white').place(x=0, y=0, relwidth=1)
                lbl_name = Label(self.qr_second_frame, text="Name:-", bg="pink", font=("times new roman", 15),
                                 fg="black")
                lbl_name.place(x=10, y=10, width=60, height=20)

                lbl_en_no = Label(self.qr_second_frame, text="Enrollment No:-", bg="pink", font=("times new roman", 15),
                                  fg="black")
                lbl_en_no.place(x=10, y=40, width=150, height=20)
                self.qr_card_frame = Frame(self.qr_main_frame, bd=2, relief=RIDGE, width=500, height=380, bg='white')
                self.qr_card_frame.place(x=340, y=155, width=299, height=190)
                self.qr_card_frame.config(bg="violet")
                self.qr_card_black_frame = Frame(self.qr_main_frame, bd=2, relief=RIDGE, width=500, height=380,
                                                 bg='white')
                self.qr_card_black_frame.place(x=0, y=345, width=645, height=40)
                self.qr_card_black_frame.config(bg="black")
                self.qr_code = Label(self.qr_main_frame, text='qr code not available', font=("times new roman", 15),
                                     bg='#3f51b5',
                                     fg='white', bd=1, relief=RIDGE)
                self.qr_code.place(x=400, y=160, width=180, height=180)

                self.coll_logo = Label(self.qr_main_frame, image=self.logo, bd=1, relief=RIDGE)
                self.coll_logo.place(x=115, y=80, width=120, height=120)
                self.qr_lbl_collage_name = Label(self.qr_card_black_frame, text='Government Polytechnic Malvan',
                                                 font=("times new roman", 15),
                                                 bg='black', fg='white').pack()
                storefilepath = "RetriveQrCode/img{0}.png".format(str(self.findId.get()))
                print(storefilepath)
                with open(storefilepath, "wb") as File:
                    File.write(mydataList[3])
                    File.close()
                self.qrimg = ImageTk.PhotoImage(file='RetriveQrCode/img{0}.png'.format(str(self.findId.get())))
                self.qr_code.config(image=self.qrimg)

                storeprofilepath = "RetriveProfileImages/profile_{0}.png".format(str(self.findId.get()))
                with open(storeprofilepath, "wb") as profileimg:
                    profileimg.write(mydataList[2])
                    profileimg.close()

                self.profileimg = ImageTk.PhotoImage(
                    file='RetriveProfileImages/profile_{0}.png'.format(str(self.findId.get())))
                # Button(homeframe,text="")
                self.displayProfile(self.profileimg)

                save = Button(self.root, text="Search", image=self.Searchicon, bg="#053246",
                                highlightbackground="green", command=self.saveIdCard).place(x=700, y=700)
                send = Button(self.root, text="Search", image=self.Searchicon, bg="#053246",
                                highlightbackground="green", command=self.FindMYId).place(x=890, y=700)

    def displayProfile(self, profileimg):
        self.myprofile = profileimg
        self.profileframe = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.profileframe.place(x=300, y=400, width=200, height=200)
        Label(self.profileframe, text="", image=self.myprofile, bg='white').place(x=300, y=400, width=200, height=200)


root = Tk()
obj = FindIdCard(root)
root.mainloop()
