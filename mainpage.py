import tkinter
from tkinter import * 
from PIL import Image, ImageTk



class main_page:
    def __init__(self,root):
        self.root = root
        self.root.title("MAIN PAGE")
        self.root.geometry("988x643+170+50")
        self.root.config(bg="#f0f3bd",relief=GROOVE)
        self.root.resizable(False,False)
        
        self.image = Image.open('online.png')

        self.image__=self.image.resize((670,545))

        self._image = ImageTk.PhotoImage(self.image__)



        label = Label(root,image=self._image,compound='left',highlightbackground="black",highlightthickness="1")
        label.place(x=10,y=83)


        top_label=Label(root,text="ONLINE ATTENDANCE\n MANAGEMENT SYSTEM",font=("Elephant",20,"bold"),bg="#ffbf69",highlightbackground="black",highlightthickness="1",width=80,relief=GROOVE).pack(side=TOP)

       
        self.image_=Image.open('admin.png')
        self.img_=self.image_.resize((180, 180))
        self.main_image=ImageTk.PhotoImage(self.img_)

        self.image=Image.open('student.png')
        self.img=self.image.resize((180, 180))
        self.main_image1=ImageTk.PhotoImage(self.img)
        
        #=============== second frame ===================*

        option_Frame = Frame(self.root, bd=1, bg='#3a5a40', relief=GROOVE,highlightbackground="black",highlightthickness=1)
        option_Frame.place(x=700,y=83,width=280,height=548)

        lbl_1=Label(option_Frame,text="CHOOSE:",font=("times new roman",20, 'bold'),bd=1,fg="#1d3557", bg='#ffb4a2', relief=GROOVE,highlightbackground="black",highlightthickness=1)
        lbl_1.place(x=70,y=30)
        
        #=============== login button ===================*

        btn_login = Button(option_Frame, text="ADMIN",font=("times new roman", 15, 'bold'),image=self.main_image, fg='white',borderwidth=10,highlightbackground="black",bg="grey",command=self.admin).place(x=30, y=90, width=210, height=205)
        btn_register= Button(option_Frame, text="STUDENT",font=("times new roman", 15,'bold'),image=self.main_image1, fg='white',borderwidth=10,highlightbackground="black",bg="grey",command=self.student1).place(x=30, y=300,width=210,height=205)
    def admin(self):
        self.root.destroy()
        import login.py
    def student1(self):
        self.root.destroy()
        import attendance.py
       
    



root = Tk()
obj = main_page(root)
root.mainloop()
