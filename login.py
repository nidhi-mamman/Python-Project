from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

class login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE || Developed By Nidhi")
        self.root.geometry("400x385")
        self.root.config(bg="white")
        self.root.resizable(False,False)

       

        self.username = StringVar()
        self.password = StringVar()

       

        #========= frame1 ========================================*
        
        login_Frame = Frame(self.root, bd=2, relief=SUNKEN, bg='cadetblue',highlightbackground="black", highlightthickness=1)
        login_Frame.place(x=10, y=15, width=380, height=350)

        lb1_details = Label(login_Frame, text="Admin Details", font=("Elephant", 30, 'bold'),bg="cadetblue").place(x=40, y=15)
        lb1_username = Label(login_Frame, text="Username:", font=("Rockwell", 20,"bold"), fg="black",bg="cadetblue").place(x=60, y=110)

        txt_username = Entry(login_Frame, textvariable=self.username, font=("times new roman", 15), bg="#ECECEC",relief=SUNKEN)
        txt_username.place(x=60, y=150,width="280",height="40")

        lb1_password = Label(login_Frame, text="Password:", font=("Rockwell", 20,"bold"), fg="black",bg="cadetblue").place(x=60, y=215)

        txt_password = Entry(root, textvariable=self.password, font=("times new roman", 15),relief=SUNKEN, bg="#ECECEC",show="*")
        txt_password.place(x=70, y=280,width="280",height="40")

        btn_login = Button(root,command=self.student,text="LOGIN", font=("Arial Rounded MT Bold", 15,'bold'),relief=GROOVE, bg="#2196f3", fg='white')
        btn_login.place(x=100, y=340, width=180, height=40)
        
    def student(self):
        uname=self.username.get()
        pwd=self.password.get()
        if (uname=="admin.host" and  pwd=="host@123"):
            messagebox.showinfo("Info","Logged in successfully")
            self.root.destroy()
            import registration.py
        else:
            messagebox.showinfo("Info","Wrong username or password!!!")
            uname.clear()
            pwd.clear()

        
    


root = Tk()
obj = login_page(root)
root.mainloop()
