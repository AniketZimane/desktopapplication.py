from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import mysql.connector as c
class ORcodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x1000")
        self.root.title("QR code generator")
        self.root.config(bg="#53868B")
        title = Label(self.root, text="Update Record", font=("times new roman", 40), bg='#053246',
                      fg='white').place(x=0, y=0, relwidth=1)
        self.genderdata = StringVar()
        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.deptdata = StringVar()
        self.var_emp_year = StringVar()
        self.var_stu_mobile = StringVar()

        self.var_stu_address = StringVar()
        self.var_stu_dob = StringVar()
        self.var_stu_gender=StringVar()
        self.var_stu_age = IntVar()
        self.lbl_image = StringVar()

        def updateRecorddatabase():
            # update_query="UPDATE Student SET Name=%s,Department=%s,Year=%s,Address=%s,DOB=%s,Gender=%s,Age=%s,Mobile_no=%s WHERE Student_ID = %s"
            messagebox.showinfo("message","updateRecorddatabase button click....")
        def updateRecord():
            # emp_frame.destroy()
            update_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
            update_frame_top = Frame(update_frame, relief=RIDGE, width=745, height=100, bg='#043256').place(x=0,y=0)
            update_frame.place(x=400, y=100, width=750, height=680)
            lbl_emp_id = Label(update_frame, text="Student_Id", font=("times new roman", 15, 'bold'),
                                 bg='white').place(
                x=170,
                y=120)
            lbl_emp_name = Label(update_frame, text="Name(full name)", font=("times new roman", 15, 'bold'),
                             bg='white').place(
            x=170,
            y=160)
            update = Label(emp_frame, text="Update Students Details", font=("goudy old style", 25), bg='#043256',
                              fg='white').place(x=0, y=0, relwidth=1)
            lbl_emp_department = Label(update_frame, text="Department", font=("times new roman", 15, 'bold'),
                                   bg='white').place(x=170, y=200)
            lbl_emp_year = Label(update_frame, text="Year", font=("times new roman", 15, 'bold'), bg='white').place(x=170,
                                                                                                             y=240)

            lbl_emp_address = Label(update_frame, text="Address", font=("times new roman", 15, 'bold'), bg='white').place(
            x=170,
            y=280)
            lbl_emp_mobile = Label(update_frame, text="Mobile No", font=("times new roman", 15, 'bold'), bg='white').place(
            x=170,
            y=320)
            lbl_emp_Dateofbirth = Label(update_frame, text="Dete of Birth", font=("times new roman", 15, 'bold'),
                                    bg='white').place(x=170, y=360)
            lbl_emp_gender = Label(update_frame, text="Gender", font=("times new roman", 15, 'bold'), bg='white').place(
            x=170,
            y=400)
            lbl_emp_age = Label(update_frame, text="Age", font=("times new roman", 15, 'bold'), bg='white').place(x=170,
                                                                                                           y=440)

            txt_emp_code = Entry(update_frame, font=("times new roman", 15), textvariable=self.var_emp_code,
                             bg='lightyellow').place(x=350, y=120)
            txt_emp_name = Entry(update_frame, font=("times new roman", 15), textvariable=self.var_emp_name,
                             bg='lightyellow').place(x=350, y=160)

            txt_emp_department = Combobox(update_frame,
                                      values=['Computer', 'Civil', 'Electrical', 'Food', 'Mechanical',
                                              'Electronic'],
                                      textvariable=self.deptdata, state='', width=30).place(x=350, y=200)
            txt_emp_year = Entry(update_frame, font=("times new roman", 15), textvariable=self.var_emp_year,
                             bg='lightyellow').place(x=350, y=240)

            txt_stu_address = Entry(update_frame, font=("times new roman", 15), textvariable=self.var_stu_address,
                                bg='lightyellow').place(x=350, y=280)
            txt_stu_mobile = Entry(update_frame, font=("times new roman", 15), textvariable=self.var_stu_mobile,
                               bg='lightyellow').place(x=350, y=320)
            txt_stu_DOB = Entry(update_frame, font=("times new roman", 15), textvariable=self.var_stu_dob,
                            bg='lightyellow').place(x=350, y=360)

            # txt_stu_gender = Entry(update_frame, font=("times new roman", 15), textvariable=self.var_stu_gender,
            #                    bg='lightyellow').place(x=600, y=400)
            txt_stu_gender = Combobox(update_frame, values=['Male', 'Feamle', 'Other'], textvariable=self.genderdata,
                                  state='',
                                  width=30).place(x=350, y=400)
            age_scale = Scale(update_frame, from_=1, to=60, orient=HORIZONTAL, variable=self.var_stu_age, bg='lightyellow')
            age_scale.place(x=350, y=440)



        def checkAvailability():
            msg = ''
            lbl_msg = Label(emp_frame, text=msg, font=("times new roman", 20, 'bold'), bg='white', fg='green').place(x=20,y=100)

            mydb = c.connect(
                host='localhost',
                user='root',
                password='123456',
                database='project_01'
            )
            mycursor = mydb.cursor()
            Select_sql_query = "Select * from studentrecord WHERE Student_ID= %s"
            Select_val = [(self.var_emp_code.get())]
            count = mycursor.execute(Select_sql_query, Select_val)
            result = mycursor.fetchone()
            if self.var_emp_code.get()=="":
                messagebox.showinfo("message", "Enter student id")
            elif (result):
                info=result
                messagebox.showinfo("message",result)
                # messagebox.showerror("message", "Record is already present")
                lbl_msg = Label(emp_frame, text=info, font=("arial", 10, 'bold'), bg='white',
                                fg='green').place(x=50, y=300)
                stu_id=self.var_emp_code.get()
                update_btn = Button(self.root, text="Update Record", width=20, height=2,
                                   font=("times new roman", 10, "bold"), background="green",
                                   command=updateRecord()).place(x=700, y=650)



            else:
                messagebox.showerror("message", "Record is not present")
                lbl1_msg = Label(emp_frame, text="Record not present", font=("times new roman", 20, 'bold'), bg='white',
                                fg='red').place(x=250, y=300)

        emp_frame = Frame(self.root, bd=2, relief=RIDGE, width=500, height=380, bg='white')
        emp_frame.place(x=400, y=100, width=750, height=680)
        emp_title = Label(emp_frame, text="Update Students Details", font=("goudy old style", 25), bg='#043256',
                          fg='white').place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(emp_frame, text="Student ID", font=("times new roman", 20, 'bold'), bg='white').place(x=150,
                                                                                                                   y=120)
        txt_emp_code = Entry(emp_frame, font=("times new roman", 20), textvariable=self.var_emp_code,
                             bg='lightyellow').place(x=300, y=120)
        check_btn=Button(self.root,text="Find Record",width=20,height=2,font=("times new roman",10,"bold"),background="green",command=checkAvailability).place(x=700,y=350)



root=Tk()
obj = ORcodeGUI(root)
root.mainloop()

#after clicking record update button record should be updated