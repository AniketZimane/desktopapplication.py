from cProfile import label
from logging import root
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from turtle import title
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage


class ORcodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x1000")
        self.root.title("QR code generator")
        # self.root.resizable(False,False)

        title = Label(self.root, text="QR Code Generator", font=("times new roman", 40), bg='#053246',
                      fg='white').place(x=0, y=0, relwidth=1)
        # -------EMPLOYEE DETAILS WINDOW------
        # -------variables

        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_department = StringVar()
        self.var_emp_year = StringVar()
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

        txt_emp_code = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_code,
                             bg='lightyellow').place(x=200, y=60)
        txt_emp_name = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_name,
                             bg='lightyellow').place(x=200, y=100)
        # txt_emp_department=ComboBox()
        txt_emp_department = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_department,
                                   bg='lightyellow').place(x=200, y=140)
        txt_emp_year = Entry(emp_frame, font=("times new roman", 15), textvariable=self.var_emp_year,
                             bg='lightyellow').place(x=200, y=180)

        btn_generate = Button(emp_frame, text="QR Generate", command=self.generate,
                              font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=600,
                                                                                                    width=180,
                                                                                                    height=30)
        btn_clear = Button(emp_frame, text="Clear", command=self.clear, font=("times new roman", 18, 'bold'),
                           bg='#607d8b', fg='white').place(x=282, y=600, width=120, height=30)

        self.msg = ''
        self.lbl_msg = Label(emp_frame, text=self.msg, font=("times new roman", 20, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        # -------Student QRCODE WINDOW------
        qr_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        qr_frame.place(x=850, y=100, width=650, height=380)
        qr_title = Label(qr_frame, text="Students IdentyCard", font=("goudy old style", 20), bg='#043256',
                         fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_frame, text='qr code not available', font=("times new roman", 15), bg='#3f51b5',
                             fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=450, y=150, width=180, height=180)

        self.coll_logo = Label(qr_frame, image="th.png", font=("times new roman", 15), bg='#3f51b5', fg='white', bd=1,
                               relief=RIDGE)
        self.coll_logo.place(x=34, y=100, width=180, height=180)
        self.qr_lbl_collage_name = Label(qr_frame, text='Government Polytechnic Malvan', font=("times new roman", 15),
                                         bg='white')
        self.qr_lbl_collage_name.place(x=225, y=350, width=300, height=15)

    def clear(self):
        self.var_emp_code.set("")
        self.var_emp_name.set("")
        self.var_emp_department.set("")
        self.var_emp_year.set("")
        self.msg = ''
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        if self.var_emp_department.get() == "" or self.var_emp_name.get() == "" or self.var_emp_code.get() == "" or self.var_emp_year.get() == "":
            messagebox.showinfo("message", "Pleae fill all the field")
            self.msg = 'All Field are required!!!!!!'
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            # -----updating notification--------
            qr_data = (
                f"Student ID:{self.var_emp_code.get()}\nStudent Name:{self.var_emp_name.get()}\nStudent Department:{self.var_emp_department.get()}\nStudent year:{self.var_emp_year.get()}")
            qr_code = qrcode.make(qr_data)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            qr_code.save(str(self.var_emp_code.get()) + ".png")
            # print(qr_code)

            # -------qr code image update-------
            self.im = ImageTk.PhotoImage(file=str(self.var_emp_code.get()) + ".png")
            self.qr_code.config(image=self.im)
            self.msg = 'QR Generated Successfully!!!!!'
            self.lbl_msg.config(text=self.msg, fg="green")


root = Tk()
obj = ORcodeGUI(root)
root.mainloop()