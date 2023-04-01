import os
import re
import math
import random
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
import mysql.connector as c
import pyscreenshot
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




class ORcodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x1000")
        self.root.title("QR code generator")
        self.root.config(bg="#53868B")
        # self.root.resizable(False,False)

        title = Label(self.root, text="Id Card Generator", font=("times new roman", 40), bg='#053246',
                      fg='white').place(x=0, y=0, relwidth=1)
        # -------EMPLOYEE DETAILS WINDOW------
        # -------variables

        self.genderdata= StringVar()
        self.var_emp_code = StringVar()
        self.var_emp_Firstname = StringVar()
        self.var_emp_Middlename=StringVar()
        self.var_emp_Lastname=StringVar()
        self.deptdata = StringVar()
        self.var_emp_year = StringVar()
        self.var_stu_mobile=StringVar()
        self.var_stu_eamil=StringVar()
        self.var_email_otp=StringVar()

        self.var_stu_address = StringVar()
        self.var_stu_dob = StringVar()
        self.var_stu_age = IntVar()
        self.getemailId=StringVar()


        self.emp_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.emp_frame.place(x=50, y=100, width=750, height=680)
        emp_title = Label(self.emp_frame, text="Students Details", font=("goudy old style", 20), bg='#043256',
                          fg='white').place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(self.emp_frame, text="Student ID", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                                   y=60)
        lbl_emp_first = Label(self.emp_frame, text="First Name", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                             y=100)
        lbl_emp_middle = Label(self.emp_frame, text="Middle Name", font=("times new roman", 15, 'bold'), bg='white').place(
            x=20,
            y=140)
        lbl_emp_last = Label(self.emp_frame, text="Last Name", font=("times new roman", 15, 'bold'), bg='white').place(
            x=20,
            y=180)
        lbl_emp_department = Label(self.emp_frame, text="Department", font=("times new roman", 15, 'bold'),
                                   bg='white').place(x=20, y=220)
        lbl_emp_year = Label(self.emp_frame, text="Year", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                             y=260)

        lbl_emp_address = Label(self.emp_frame, text="Address", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                                   y=300)
        lbl_emp_mobile = Label(self.emp_frame, text="Mobile No", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                                   y=340)
        lbl_emp_Dateofbirth = Label(self.emp_frame, text="Dete of Birth", font=("times new roman", 15, 'bold'),
                                    bg='white').place(x=20, y=380)
        lbl_emp_email = Label(self.emp_frame, text="Email", font=("times new roman", 15, 'bold'),
                                    bg='white').place(x=450, y=380)
        lbl_otp = Label(self.emp_frame, text="OTP", font=("times new roman", 15, 'bold'),
                              bg='white').place(x=450, y=420)
        lbl_emp_gender = Label(self.emp_frame, text="Gender", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                                 y=420)
        lbl_emp_age = Label(self.emp_frame, text="Age", font=("times new roman", 15, 'bold'), bg='white').place(x=20, y=460)


        txt_emp_code = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_emp_code,
                             bg='lightyellow').place(x=200, y=60)
        txt_emp_first = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_emp_Firstname,
                             bg='lightyellow').place(x=200, y=100)
        txt_emp_middle = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_emp_Middlename,
                             bg='lightyellow').place(x=200, y=140)
        txt_emp_last = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_emp_Lastname,
                             bg='lightyellow').place(x=200, y=180)

        # txt_emp_department = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_department,
        #                            bg='lightyellow').place(x=200, y=140)

        txt_emp_department = Combobox(root, values=['Computer', 'Civil','Electrical','Food','Mechanical','Electronic'], textvariable=self.deptdata, state='', width=30).place(x=250, y=325)
        txt_emp_year = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_emp_year,
                             bg='lightyellow').place(x=200, y=260)

        txt_stu_address = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_stu_address,
                                bg='lightyellow').place(x=200, y=300)
        txt_stu_mobile = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_stu_mobile,
                                bg='lightyellow').place(x=200, y=340)
        txt_stu_DOB = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_stu_dob,
                            bg='lightyellow').place(x=200, y=380)

        # txt_stu_gender = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_stu_gender,
        #                        bg='lightyellow').place(x=200, y=340)
        txt_stu_gender = Combobox(root, values=['Male', 'Feamle','Other'], textvariable=self.genderdata, state='', width=30).place(x=250, y=530)
        txt_stu_email = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_stu_eamil,
                              bg='lightyellow').place(x=520, y=380)
        otpenty = Entry(self.emp_frame, font=("times new roman", 15), textvariable=self.var_email_otp,
                              bg='lightyellow').place(x=520, y=420)
        age_scale = Scale(self.emp_frame, from_=1, to=60, orient=HORIZONTAL, variable=self.var_stu_age, bg='lightyellow')
        age_scale.place(x=200, y=460)
        sendotpbtn = Button(self.emp_frame, text="Send OTP", font=("times new roman", 13),
                           bg='Green', command=self.sendOTP).place(x=550, y=470)


        age = self.var_stu_age.get()

        # btn_generate = Button(emp_frame, text="QR Generate", command=self.generate,
        #                       font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=600,
        #                                                                                             width=180,
        #                                                                                             height=30)
        btn_clear = Button(self.emp_frame, text="Clear", command=self.clear, font=("times new roman", 18, 'bold'),
                           bg='#607d8b', fg='white').place(x=282, y=600, width=120, height=30)

        self.msg = ''
        self.lbl_msg = Label(self.emp_frame, text=self.msg, font=("times new roman", 20, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=510, relwidth=1)

        # -------Student QRCODE WINDOW------
        self.qr_main_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.qr_main_frame.place(x=850, y=100, width=650, height=390)
        self.qr_main_frame.config(bg="orange")

        # -------Student Photo upload frame------
        self.photo_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.photo_frame.place(x=490, y=150, width=300, height=300)
        self.photo_frame.config(bg="white")
        self.lbl = Label(root)
        # self.lbl.pack(side=CENTER)
        self.lbl.place(x=490,y=150)
        self.upload_image=Button(self.root,text="Upload photo",width=40,height=3,font=("times new roman",10,"bold"),command=self.uploadPhoto).place(x=494,y=387)

        # self.dept_name=''
        # self.lbl_msg=Label(self.qr_main_frame,text=self.dept_name,font=("times new roman",20,'bold'),bg='orange',fg='black')
        # self.lbl_msg.place(x=80,y=220,width=280,height=70)

        self.qr_second_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.qr_second_frame.place(x=1205, y=145, width=290, height=110)
        self.qr_second_frame.config(bg="pink")

        lbl_name = Label(self.root, text="Name:-", bg="pink", font=("times new roman", 15), fg="black")
        lbl_name.place(x=1213, y=160, width=60, height=20)

        lbl_en_no = Label(self.root, text="Enrollment No:-", bg="pink", font=("times new roman", 15), fg="black")
        lbl_en_no.place(x=1207, y=180, width=150, height=20)

        self.qr_card_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.qr_card_frame.place(x=1205, y=255, width=290, height=190)
        self.qr_card_frame.config(bg="violet")

        self.qr_card_black_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.qr_card_black_frame.place(x=855, y=445, width=640, height=40)
        self.qr_card_black_frame.config(bg="black")

        qr_title = Label(self.qr_main_frame, text="Students IdentyCard", font=("goudy old style", 20), bg='#043256',
                         fg='white').place(x=0, y=0, relwidth=1)

        # self.qr_code=Label(self.qr_card_frame,text='qr code not available',font=("times new roman",15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        # self.qr_code.place(x=450,y=160,width=180,height=180)

        self.qr_code = Label(self.root, text='qr code not available', font=("times new roman", 15), bg='#3f51b5',
                             fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=1270, y=260, width=180, height=180)

        self.logo = PhotoImage(file='logo.png')
        self.coll_logo = Label(self.qr_main_frame, image=self.logo, bd=1, relief=RIDGE)
        self.coll_logo.place(x=115, y=80, width=120, height=120)
        self.qr_lbl_collage_name = Label(self.root, text='Government Polytechnic Malvan', font=("times new roman", 15),
                                         bg='black', fg='white')
        self.qr_lbl_collage_name.place(x=1060, y=455, width=300, height=20)
    def sendOTP(self):

        emailid = self.var_stu_eamil.get()
        try:
            if not emailid == "":

                digits = "0123456789"
                self.otp = ""
                for i in range(6):
                    self.otp += digits[math.floor(random.random() * 10)]

                otpwithmess = self.otp + " is your OTP"
                msg = otpwithmess
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("ad.developer1604@gmail.com", "elerivkphnknpava")
                # emailid = self.var_stu_eamil.get()
                s.sendmail('&&&&&&&&&&&', emailid, msg)
                messagebox.showinfo("Messsage","OTP send successfully")
                verifybtn = Button(self.emp_frame, text="Verify", font=("times new roman", 13),bg='Green', command=self.GenerateQRBtn).place(x=640, y=470)
        except:
            messagebox.showerror("Error","Server serror....try after some time")

    def GenerateQRBtn(self):
        a = self.var_email_otp.get()
        if a == self.otp:
            print("Verified")
            messagebox.showinfo("Message","OTP verified successfully")
            btn_generate = Button(self.emp_frame, text="QR Generate", command=self.generate,
                                      font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=600,
                                                                                                            width=180,
                                                                                                            height=30)
        else:
            messagebox.showerror("message","Wrong OTP")

    def sendEmail(self):
        sendemailwindow = Toplevel(root)
        sendemailwindow.geometry("600x500+500+200")
        sendemailwindow.resizable(False, False)
        sendemailwindow.config(bg="#53868B")
        sendemailwindow.title("sendemailwindow_page")
        toptitle = Frame(sendemailwindow, width=600, height=100, bg="black")
        toptitle.place(x=0, y=0)
        label = Label(toptitle, text="Send Id card", font="impact 30", bg="black", fg="white")
        label.place(x=190, y=20)
        lableemailid=Label(sendemailwindow,text="Email id",font="impact 20",bg="#53868B").place(x=100,y=200)
        self.emailiduser=self.getemailId.get()
        emailfield=Entry(sendemailwindow,width=22,textvariable=self.getemailId,font="arial 20",background='lightgray',fg='black').place(x=210,y=200)

        sendButton=Button(sendemailwindow,text="Send",bg="green",fg="white",font=("times new roman bold", 15),command=self.sendEmailtoclient).place(x=280,y=300)
        sendemailwindow.mainloop()
    def saveIdCard(self):
        self.image = pyscreenshot.grab(bbox=(1020, 120, 1900, 655))  # x1,x2,y1,y2 y1=width y2=height
        # self.image.show()
        self.id=self.var_emp_code.get()
        self.image.save('GenerateIdCard/img{0}.png'.format(str(self.id)))
        messagebox.showinfo("info","Your card save successfuly........")
    def uploadPhoto(self):
        self.fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file",
                                         filetypes=(("JPG file", "*.jpg"), \
                                                    ("PNG file", "*.png"), ("All files", "*.*")))

        self.img = Image.open(self.fln)
        self.img.thumbnail((300, 300))
        self.img = ImageTk.PhotoImage(self.img)
        self.lbl.configure(image=self.img)
        self.lbl.image = self.img
        print(self.img)
        with open(self.fln, "rb") as File:
            self.binarydata = File.read()

    def sendEmailtoclient(self):
        try:
            fromaddr = "ad.developer1604@gmail.com"
            toaddr =self.getemailId.get()
            print(toaddr)
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = 'Student identy card'
            body = 'Welcome to smart attendance management system This card generate from smart attenance management system'
            msg.attach(MIMEText(body, 'plain'))
            filename = "GenerateIdCard/img{0}.png".format(str(self.var_emp_code.get()))
            print(filename)
            attachment = open(filename, 'rb')
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment;filename=%s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, "elerivkphnknpava")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            messagebox.showinfo("Message","Email send successfully")
            s.quit()
        except:
            messagebox.showerror("Error","Server serror....\nTry after some time\nMake sure you have an active internetconnection")
    def clear(self):
        self.var_emp_code.set("")
        self.deptdata.set("")
        self.genderdata.set("")
        self.var_stu_address.set("")
        self.var_stu_mobile.set("")
        self.var_stu_age.set(0)
        self.var_emp_year.set("")
        self.var_emp_Lastname.set("")
        self.var_emp_Middlename.set("")
        self.var_emp_Firstname.set("")
        self.msg = ''
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        mydb = c.connect(
                host='localhost',
                user='root',
                password='123456',
                database='project_01'
            )
        mycursor = mydb.cursor()
        Select_sql_query = "Select * from studentrecord WHERE Student_ID= %s"
        Select_val=[(self.var_emp_code.get())]
        count=mycursor.execute(Select_sql_query, Select_val)
        result=mycursor.fetchone()
        emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Z|a-z]{2,}\b'
        mobileregex = r'\d{10}'
        # nameregex = r'\b[A-Za-z]'
        firstregex = r'[A-Za-z]+'
        middleregex = r'[A-Za-z]+'
        lastregex = r'[A-Za-z]+'
        idregex = '\d{10}'
        if(result):
            messagebox.showerror("message", "Record is already present")
        else:
            if self.deptdata.get() == "" or self.var_emp_Firstname.get() == "" or self.var_emp_Middlename.get() == "" or self.var_emp_Lastname.get()=="" or self.var_emp_code.get() == "" or self.var_emp_year.get() == "" or self.var_stu_address.get() == "" or self.var_stu_dob.get() == "" or self.genderdata.get() == "" or self.var_stu_age.get() == "":
                messagebox.showinfo("message", "Please fill all the field")
                self.msg = 'All Field are required!!!!!!'
                self.lbl_msg.config(text=self.msg, fg="red")

            elif not re.fullmatch(firstregex,self.var_emp_Firstname.get()):
                messagebox.showinfo("message", "Please Enter correct First name(e.g.Ramesh)")

            elif not re.fullmatch(middleregex,self.var_emp_Middlename.get()):
                messagebox.showinfo("message", "Please Enter correct Middle name(e.g.Suresh)")

            elif not re.fullmatch(lastregex,self.var_emp_Lastname.get()):
                messagebox.showinfo("message", "Please Enter correct Surname name(e.g.Parab)")

            elif not re.fullmatch(idregex,self.var_emp_code.get()):
                messagebox.showinfo("message", "Please Enter correct student id(1234567890)")
            else:
            # -----updating notification--------
                emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za--z0-9._]+\.[A-Z|a-z]{2,}\b'
                mobileregex = r'\d{10}'
                nameregex = r'^([a-z]+)([a-z]+)*([a-z]+)*$'
                idregex = '\d{10}'
                qr_data = (
                f"Student ID:{self.var_emp_code.get()}\nStudent Name:{self.var_emp_Firstname.get()+' '+self.var_emp_Lastname.get()}\nStudent Department:{self.deptdata.get()}\nStudent year:{self.var_emp_year.get()} \nStudent Address:{self.var_stu_address.get()}\nStudent DOB:{self.var_stu_dob.get()}\nStudent Gender:{self.genderdata.get()}\nStudent Age:{self.var_stu_age.get()}")
                qr_code = qrcode.make(qr_data)
                qr_code = resizeimage.resize_cover(qr_code, [180, 180])
                qr_code.save(str(self.var_emp_code.get()) + ".png")
            # print(qr_code)


            # -------qr code image update-------
                self.im = ImageTk.PhotoImage(file=str(self.var_emp_code.get()) + ".png")
                imgpathqr = "C:/Users/Aniket/PycharmProjects/FinalYearProject/"+str(self.var_emp_code.get()) + ".png"
                self.qr_code.config(image=self.im)
                self.msg = 'QR Generated Successfully!!!!!'
                self.lbl_msg.config(text=self.msg, fg="green")
                print(imgpathqr)
                with open(imgpathqr,"rb") as myimg:
                    self.binarycodeqr=myimg.read()
                self.print_dept = self.deptdata.get()+"\nEngineering"
                lbl_dept = Label(self.qr_main_frame, text=self.print_dept, bg="orange", font=("times new roman", 20),
                             fg="black")
                lbl_dept.place(x=50, y=220, width=280, height=70)

            # lbl_name=Label(self.qr_second_frame,text="Name: ",bg="orange",font=("times new roman",15),fg="black")
            # lbl_name.place(x=360,y=70,width=60,height=20)

                self.fullname = self.var_emp_Firstname.get() + " " + self.var_emp_Lastname.get()
                lbl_name_card = Label(self.root, text=self.fullname, bg="pink", font=("times new roman", 15), fg="black")
                lbl_name_card.place(x=1273, y=160, width=150, height=20)

            # lbl_en_no=Label(self.qr_main_frame,text="Enrollment No:- ",bg="orange",font=("times new roman",15),fg="black")
            # lbl_en_no.place(x=290,y=110,width=200,height=20)

                self.print_code = self.var_emp_code.get()
                lbl_en_no_card = Label(self.root, text=self.print_code, bg="pink", font=("times new roman", 15), fg="black")
                lbl_en_no_card.place(x=1357, y=180, width=130, height=20)


#----------------------------------------------->INSERT DATA INTO DATABASE<--------------------------------------

            # mydb = c.connect(
            #     host='localhost',
            #     user='root',
            #     password='123456',
            #     database='project_01'
            # )
            # mycursor = mydb.cursor()
            # mycursor = mydb.cursor()
            # try:
                insert_sql_query = "INSERT INTO studentrecord(Student_ID,Name,Department,Year,Address,DOB,Gender,Age,Mobile_no,Photo,QRImage) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (self.var_emp_code.get(),self.fullname,self.deptdata.get(),self.var_emp_year.get(),self.var_stu_address.get(),self.var_stu_dob.get(),self.genderdata.get(),self.var_stu_age.get(),self.var_stu_mobile.get(),self.binarydata,self.binarycodeqr)
                mycursor.execute(insert_sql_query, val)
                mydb.commit()
                # saveicon=PhotoImage(file='save.png')
                # sendicon=PhotoImage(file='sendmail.png')
                # Button(root,text='',image=saveicon).place(x=900,y=600)
                self.saveicon = PhotoImage(file="save.png")

                save = Button(self.root, text="Search", image=self.saveicon, bg="#053246",
                              highlightbackground="green", command=self.saveIdCard).place(x=1360, y=15)
                self.sendicon = PhotoImage(file="sendmail.png")
                send = Button(self.root, text="Search", image=self.sendicon, bg="#053246",
                              highlightbackground="green", command=self.sendEmail).place(x=1450, y=15)


            # except:
            #     messagebox.showerror("error","Unable to fill the data\nTry after some time")



root = Tk()
obj = ORcodeGUI(root)
root.mainloop()