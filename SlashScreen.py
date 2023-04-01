from tkinter import *
slash_root=Tk()
slash_root.title("Loading........")
slash_root.geometry("1500x1000")
slash_lable=Label(slash_root,text="Slash screen",font=("helvetica",18)).pack(pady=20)

def main_window():
    slash_root.destroy()
    root=Tk()
    root.title("Smart Attendance")
    root.iconbitmap("th.png")
    root.geometry("500x500+200+200")

slash_root.after(3000,main_window)
slash_root.mainloop()