
from tkinter import *
from tkinter import messagebox
from ORcodeGUI import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
import mysql.connector as c





























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

        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_department = StringVar()
        self.var_emp_year = StringVar()

        self.var_stu_address = StringVar()
        self.var_stu_dob = StringVar()
        self.var_stu_gender = StringVar()
        self.var_stu_age = IntVar()

        emp_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        emp_frame.place(x=50, y=100, width=750, height=680)
        emp_title = Label(emp_frame, text="Students Details", font=("goudy old style", 20), bg='#043256',
                          fg='white').place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(emp_frame, text="Student ID", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                                   y=60)
        lbl_emp_name = Label(emp_frame, text="Name", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                             y=100)
        lbl_emp_department = Label(emp_frame, text="Department", font=("times new roman", 15, 'bold'),
                                   bg='white').place(x=20, y=140)
        lbl_emp_year = Label(emp_frame, text="Year", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                             y=180)

        lbl_emp_address = Label(emp_frame, text="Address", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                                   y=220)
        lbl_emp_Dateofbirth = Label(emp_frame, text="Dete of Birth", font=("times new roman", 15, 'bold'),
                                    bg='white').place(x=20, y=300)
        lbl_emp_gender = Label(emp_frame, text="Gender", font=("times new roman", 15, 'bold'), bg='white').place(x=20,
                                                                                                                 y=340)
        lbl_emp_age = Label(emp_frame, text="Age", font=("times new roman", 15, 'bold'), bg='white').place(x=20, y=380)

        txt_emp_code = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_code,
                             bg='lightyellow').place(x=200, y=60)
        txt_emp_name = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_name,
                             bg='lightyellow').place(x=200, y=100)

        txt_emp_department = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_department,
                                   bg='lightyellow').place(x=200, y=140)
        txt_emp_year = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_year,
                             bg='lightyellow').place(x=200, y=180)

        txt_stu_address = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_stu_address,
                                bg='lightyellow').place(x=200, y=220)
        txt_stu_DOB = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_stu_dob,
                            bg='lightyellow').place(x=200, y=300)

        txt_stu_gender = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_stu_gender,
                               bg='lightyellow').place(x=200, y=340)
        age_scale = Scale(emp_frame, from_=1, to=60, orient=HORIZONTAL, variable=self.var_stu_age, bg='lightyellow')
        age_scale.place(x=200, y=380)
        age = self.var_stu_age.get()

        btn_generate = Button(emp_frame, text="QR Generate", command=self.generate,
                              font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=600,
                                                                                                    width=180,
                                                                                                    height=30)
        btn_clear = Button(emp_frame, text="Clear", command=self.clear, font=("times new roman", 18, 'bold'),
                           bg='#607d8b', fg='white').place(x=282, y=600, width=120, height=30)

        self.msg = ''
        self.lbl_msg = Label(emp_frame, text=self.msg, font=("times new roman", 20, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=510, relwidth=1)

        # -------Student QRCODE WINDOW------
        self.qr_main_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        self.qr_main_frame.place(x=850, y=100, width=650, height=390)
        self.qr_main_frame.config(bg="orange")

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

        # print_dept=self.var_emp_department.get()
        # lbl_dept=Label(self.qr_main_frame,text="Computer Engineering\nDepartment",font=("times new roman",20),bg='orange')
        # lbl_dept.place(x=80,y=220,width=280,height=70)

    def clear(self):
        self.var_emp_code.set("")
        self.var_emp_name.set("")
        self.var_emp_department.set("")
        self.var_emp_year.set("")
        self.msg = ''
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        if self.var_emp_department.get() == "" or self.var_emp_name.get() == "" or self.var_emp_code.get() == "" or self.var_emp_year.get() == "" or self.var_stu_address.get() == "" or self.var_stu_dob.get() == "" or self.var_stu_gender.get() == "" or self.var_stu_age.get() == "":
            messagebox.showinfo("message", "Pleae fill all the field")
            self.msg = 'All Field are required!!!!!!'
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            # -----updating notification--------
            qr_data = (
                f"Student ID:{self.var_emp_code.get()}\nStudent Name:{self.var_emp_name.get()}\nStudent Department:{self.var_emp_department.get()}\nStudent year:{self.var_emp_year.get()} \nStudent Address:{self.var_stu_address.get()}\nStudent DOB:{self.var_stu_dob.get()}\nStudent Gender:{self.var_stu_gender.get()}\nStudent Age:{self.var_stu_age.get()}")
            qr_code = qrcode.make(qr_data)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            qr_code.save(str(self.var_emp_code.get()) + ".png")
            # print(qr_code)

            # -------qr code image update-------
            self.im = ImageTk.PhotoImage(file=str(self.var_emp_code.get()) + ".png")
            self.qr_code.config(image=self.im)
            self.msg = 'QR Generated Successfully!!!!!'
            self.lbl_msg.config(text=self.msg, fg="green")

            self.print_dept = self.var_emp_department.get()
            lbl_dept = Label(self.qr_main_frame, text=self.print_dept, bg="orange", font=("times new roman", 20),
                             fg="black")
            lbl_dept.place(x=50, y=220, width=280, height=70)

            # lbl_name=Label(self.qr_second_frame,text="Name: ",bg="orange",font=("times new roman",15),fg="black")
            # lbl_name.place(x=360,y=70,width=60,height=20)

            self.print_name = self.var_emp_name.get()
            lbl_name_card = Label(self.root, text=self.print_name, bg="pink", font=("times new roman", 15), fg="black")
            lbl_name_card.place(x=1273, y=160, width=150, height=20)

            # lbl_en_no=Label(self.qr_main_frame,text="Enrollment No:- ",bg="orange",font=("times new roman",15),fg="black")
            # lbl_en_no.place(x=290,y=110,width=200,height=20)

            self.print_code = self.var_emp_code.get()
            lbl_en_no_card = Label(self.root, text=self.print_code, bg="pink", font=("times new roman", 15), fg="black")
            lbl_en_no_card.place(x=1357, y=180, width=130, height=20)

#----------------------------------------------->INSERT DATA INTO DATABASE<--------------------------------------

            mydb = c.connect(
                host='localhost',
                user='root',
                password='123456',
                database='project_01'
            )
            mycursor = mydb.cursor()
            insert_sql_query = "INSERT INTO studentrecord(Student_ID,Name,Department,Year,Address,DOB,Gender,Age) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (self.var_emp_code.get(),self.var_emp_name.get(),self.var_emp_department.get(),self.var_emp_year.get(),self.var_stu_address.get(),self.var_stu_dob.get(),self.var_stu_gender.get(),self.var_stu_age.get())
            mycursor.execute(insert_sql_query, val)
            mydb.commit()


root = Tk()
obj = ORcodeGUI(root)
root.mainloop()