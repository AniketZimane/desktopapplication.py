from tkinter import *

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")
        self.root.title("DashBoard of attendance management system")
        self.root.config(bg="#adcbce")
        black_frame=Frame(self.root,relief=RIDGE,width=200,height=1080,bg='#88b3b8')
        black_frame.place(x=0,y=0,width=300,height=1080)
        top_light_shade_frame=Frame(self.root,relief=RIDGE,width=1920,height=40,bg='#d2e2e4').place(x=300,y=0)
        top_light_shade_frame_title=Label(top_light_shade_frame,text="Attendanse Management System", font=("times new roman", 15, 'bold'), bg='#d2e2e4').place(x=350,y=10)
        logo_image=Label()
        logo_attbtn =Button(root,width=20,height=2,text="Mark Attendance",font="arial 20 bold",bg="red",bd="10").place(x=400,y=100)
        btnState = False
        def switch():
            global btnState
            if btnState is True:
                # create animated Navbar closing:
                for x in range(301):
                    navRoot.place(x=-x, y=0)
                    top_light_shade_frame.update()

                # resetting widget colors:

                homeLabel.config(bg="#adcbce")
                top_light_shade_frame.config(bg="#adcbce")
                root.config(bg="gray17")

                # turning button OFF:
                btnState= False
            else:
                # make root dim:
                # brandLabel.config(bg=color["nero"], fg="#5F5A33")
                homeLabel.config(bg="nero")
                top_light_shade_frame.config(bg="nero")
                root.config(bg="nero")

                # created animated Navbar opening:
                for x in range(-300, 0):
                    navRoot.place(x=x, y=0)
                    top_light_shade_frame.update()

                # turing button ON:
                btnState= True

        navIcon = PhotoImage(file="theeline.png")
        closeIcon = PhotoImage(file="close.png")

        # topFrame = Frame(root, bg="#d2e2e4")
        # topFrame.pack(side="top", fill=X)

        # Header label text:
        homeLabel = Label(top_light_shade_frame, text="PE", font="Bahnschrift 15", bg="orange", fg="gray17", height=2,
                             padx=20)
        homeLabel.pack(side="right")

        # Main label text:

        # Navbar button:
        navbarBtn = Button(top_light_shade_frame, image=navIcon, bg="#adcbce", activebackground="orange", bd=0,
                              padx=20, command=switch)
        navbarBtn.place(x=10, y=10)

        # setting Navbar frame:
        navRoot = Frame(root, bg="gray17", height=1000, width=300)
        navRoot.place(x=-300, y=0)
        Label(navRoot, font="Bahnschrift 15", bg="orange", fg="black", height=2, width=300, padx=20).place(
            x=0, y=0)

        # set y-coordinate of Navbar widgets:
        y = 80
        # option in the navbar:
        options = ["Profile", "Settings", "Help", "About", "Feedback"]
        # Navbar Option Buttons:
        for i in range(5):
            Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg="orange",
                      activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
            y += 40

        # Navbar Close Button:
        closeBtn = Button(navRoot, image=closeIcon, bg="orange", activebackground="orange", bd=0,
                             command=switch)
        closeBtn.place(x=250, y=10)

        # window in mainloop:
        root.mainloop()



root = Tk()
obj = HomePage(root)
root.mainloop()
