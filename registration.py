import tkinter
from tkinter import *
from tkinter import messagebox
from mysql import connector
from tkinter import ttk
ab=Tk() 
roll_no=StringVar()
name=StringVar()
contact=StringVar()
email=StringVar()
address=StringVar()
l_8=StringVar()
var=StringVar()

#=================main-frame==============*

ab.title("MAIN PAGE || Developed By Nidhi ")
ab.geometry("600x600+170+50")
ab.config(bg="#d0f4de")
ab.resizable(False, False)

#=================add function=============*

def add():
    conn=connector.connect(
        user='root',
        password='root@95&30',
        host='127.0.0.1',
        port='3306',
        database='register_stud')
    mycursor=conn.cursor()
    roll_no=e_1.get()
    name=e_2.get()
    contact=e_3.get() 
    email=e_4.get()
    address=e_5.get() 
    branch=l_8.get() 
    gender=var.get() 
    mycursor.execute("insert into register_details values(%s,%s,%s,%s,%s,%s,%s)",(roll_no,name,contact,email,address,branch,gender))
    messagebox.showinfo("Added","Successfully")
    conn.commit()

#=============clear function===========*

def clear():
    e_1.delete(0,END)
    e_2.delete(0,END)
    e_3.delete(0,END)
    e_4.delete(0,END)
    e_5.delete(0,END)
    var.set(0)
    l_8.set(" ")

#==============update  function=========*

def update():
    if (e_1.get()=="" or e_2.get()==""):
        messagebox.showerror("Error","All fields are required")
    
    else:
            update=messagebox.askyesno("Update","Are you sure to update?",parent=ab)
            if update>0:
                con=connector.connect(user='root',password='root@95&30',host='127.0.0.1',port='3306',database='register_stud',autocommit=True)
                mycursor=con.cursor()
                roll_no=e_1.get()
                name=e_2.get()
                contact=e_3.get() 
                email=e_4.get()
                address=e_5.get() 
                branch=l_8.get() 
                gender=var.get() 
                mycursor.execute("update register_details set name=%s,contact=%s,email=%s,address=%s,branch=%s,gender=%s  where roll_no=%s",(name,contact,email,address,branch,gender,roll_no))
            else:
                if not update:
                    return
            con.commit()
            messagebox.showinfo("updated","successfully")


#===================record function===========*

def record():

    #==================table main-frame===================*
    root=Tk()
    root.title("record table")
    root.config(bg="white")
    root.geometry("500x500")
    table_frame=Label(root,text="STUDENT DATABASE",bg="cadetblue",fg="black",font=("elephant",20,"bold"))
    table_frame.pack(fill=X)
    scroll_x = Scrollbar(root, orient=HORIZONTAL)
    scroll_y = Scrollbar(root, orient=VERTICAL)
    Student_table = ttk.Treeview(root,columns=("roll_no", "name", "contact", "email", "address", "branch","gender"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=Student_table.xview)
    scroll_y.config(command=Student_table.yview)
    Student_table.heading("roll_no", text="Roll no")
    Student_table.heading("name", text="Name")
    Student_table.heading("contact", text="Contact")
    Student_table.heading("email", text="Email")
    Student_table.heading("address", text="Address")
    Student_table.heading("branch", text="Branch")
    Student_table.heading("gender", text="Gender")
    Student_table['show'] ='headings'
    Student_table.column("roll_no", width=50)
    Student_table.column("name", width=150)
    Student_table.column("contact", width=130)
    Student_table.column("email", width=200)
    Student_table.column("address", width=200)
    Student_table.column("branch", width=100)
    Student_table.column("gender", width=100)
    Student_table.pack(fill=BOTH, expand=1)
    conn=connector.connect(
         user='root',
         password='root@95&30',
        host='127.0.0.1',
        port='3306',
        database='register_stud')
    mycursor=conn.cursor()
    query="select * from register_details"
    mycursor.execute(query)
    data=mycursor.fetchall()
    if len(data)!=0:
        Student_table.delete(*Student_table.get_children())
        for i in  data:
            Student_table.insert("",END,values=i)
        conn.commit()
    conn.close()

#===================registration form page=======================*

frame=Frame(ab,bd=1,bg="#a2d2ff", highlightbackground="black",highlightthickness=1)
frame.place(x=40,y=20,width=515,height=500)

l_0 = Label(frame,text="Registration form",bg="#457b9d",relief=GROOVE,font=("elephant",25,"bold"))
l_0.pack(fill=X)


l_1 = Label(frame, text="ROLL NO:",  bg="#a2d2ff", font=("arial black", 20,"bold"))
l_1.place(x=30,y=80)

e_1 = Entry(frame,textvariable=roll_no,bg='white',width="45")
e_1.place(x=195,y=90,height="25")

l_2 = Label(frame, text="NAME:", bg="#a2d2ff", font=("arial black", 20,"bold"))
l_2.place(x=30,y=130)

e_2 = Entry(frame,textvariable=name,bg='white',width="45")
e_2.place(x=195,y=140,height="25")

l_3 = Label(frame, text="CONTACT:", bg="#a2d2ff", font=("arial black", 20,"bold"))
l_3.place(x=28, y=180)

e_3 = Entry(frame,textvariable=contact, bg='white',width="45")
e_3.place(x=195, y=190,height="25")

l_4 = Label(frame, text="EMAIL:", bg="#a2d2ff", font=("arial black", 20,"bold"))
l_4.place(x=30, y=230)

e_4 = Entry(frame,textvariable=email,bg='white',width="45")
e_4.place(x=195, y=240,height="25")


l_5 = Label(frame, text="ADDRESS:",  bg="#a2d2ff", font=("arial black", 20,"bold"))
l_5.place(x=30,y=280)

e_5=Entry(frame,textvariable=address,bg='white',width="45")
e_5.place(x=195,y=290,height="25")

l_6 = Label(frame, text="GENDER:", font=("arial black", 20,"bold"),bg="#a2d2ff")
l_6.place(x=30,y=340)
var= IntVar()
Radiobutton(frame,text="Male",padx = 30,variable=var,value=1,bg="white").place(x=200,y=350)
Radiobutton(frame,text="Female",padx = 35, variable=var,value=2,bg="white").place(x=315,y=350)
l_7 = Label(frame, text="BRANCH:", font=("arial black", 20,"bold"),bg="#a2d2ff")
l_7.place(x=30,y=400)
l_8= StringVar(frame)
l_8.set("Select one") 
e_8= OptionMenu(frame,l_8,"CSE","IT","ECE","ME","EE")
e_8.pack()
e_8.place(x=197,y=410,width="120")

#=================buttons==================*

Button(ab,text='Add',width=10,height=2,relief=GROOVE,bg='blue',fg='white',cursor="hand2",command=add).place(x=65,y=545)
Button(ab,text='Update',width=10,height=2,relief=GROOVE,bg='blue',fg='white',cursor="hand2",command=update).place(x=195,y=545)
Button(ab,text='Record',width=10,height=2,relief=GROOVE,bg='blue',fg='white',cursor="hand2",command=record).place(x=325,y=545)
Button(ab,text='Clear',width=10,height=2,relief=GROOVE,bg='blue',fg='white',cursor="hand2",command=clear).place(x=455,y=545)
ab.mainloop()
