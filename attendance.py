import tkinter as tk
from tkinter import *
from  tkinter import messagebox
from datetime import datetime
from mysql import connector
from PIL  import Image,ImageTk
from tkinter import ttk
root=Tk()
root.geometry('495x500+170+50')
roll_no=StringVar()
time=StringVar()
status=StringVar()


def add():
        conn=connector.connect(
        user='root',
        password='root@95&30',
        host='127.0.0.1',
        port='3306',
        database='register_stud')
        mycursor=conn.cursor()
        roll_no=e_1.get()
        time = datetime.now()
        time.strftime("%d/%m/%Y %H:%M:%S")
        status=var.get()
        mycursor.execute("insert into att_rec value(%s,%s,%s)",(roll_no,time,status))
        messagebox.showinfo("attendance","submitted")
        conn.commit()

def show():
    root=Tk()
    root.title("attendance record")
    root.config(bg="white")
    root.geometry("500x500")
    table_frame=Label(root,text="STUDENT DATABASE",bg="cadetblue",fg="black",font=("elephant",20,"bold"))
    table_frame.pack(fill=X)
    scroll_x = Scrollbar(root, orient=HORIZONTAL)
    scroll_y = Scrollbar(root, orient=VERTICAL)
    Student_table = ttk.Treeview(root,columns=("roll_no","time","status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=Student_table.xview)
    scroll_y.config(command=Student_table.yview)
    Student_table.heading("roll_no", text="Roll no")
    Student_table.heading("time", text="Time")
    Student_table.heading("status", text="Status")
    Student_table['show'] ='headings'
    Student_table.column("roll_no", width=50)
    Student_table.column("time", width=80)
    Student_table.column("status", width=20)
    Student_table.pack(fill=BOTH, expand=1)
    conn=connector.connect(
        user='root',
        password='root@95&30',
        host='127.0.0.1',
        port='3306',
        database='register_stud')
    mycursor=conn.cursor()
    query="select * from att_rec"
    mycursor.execute(query)
    data=mycursor.fetchall()
    if len(data)!=0:
        Student_table.delete(*Student_table.get_children())
        for i in  data:
            Student_table.insert("",END,values=i)
        conn.commit()
    conn.close()

root.title("Attendance Page")
root.config(bg="#edf2f4")

frame=Frame(root,bd=1,bg="#83c5be",relief=GROOVE, highlightbackground="black",highlightthickness=1)
frame.place(x=15,y=10,width=450,height=450)

image = Image.open('attendance.png')
image__=image.resize((50,50))
_image = ImageTk.PhotoImage(image__)
label = Label(root,image=_image,compound='center',highlightbackground="black",highlightthickness="1")
label.pack()

label=Label(frame,text="Mark your attendance",bg="#83c5be",relief=GROOVE,highlightbackground="black",font=("elephant",20)).place(x=90,y=50)

lable_1=Label(frame,text="ROLL NO:",bg='#83c5be',font=("arial",20,"bold")).place(x=95,y=120)
e_1=Entry(frame,bg="#ECECEC",font=("arial",15))
e_1.place(x=95,y=160)


lable_3=Label(frame,text="LOGIN-TIME:",bg='#83c5be',font=("arial",20,"bold")).place(x=95,y=200)
btn_time=Button(frame,text="time and date:",bg="#ECECEC",width="20",fg="lightgrey",font=("arail",15))
btn_time.place(x=95,y=240)

lable_4 = Label(frame, text="STATUS:",bg='#83c5be',font=("arial", 20,"bold"))
lable_4.place(x=95,y=300)
var= IntVar()
Radiobutton(frame,text="Present",width=10,variable=var,value=1,font=("arial",10,"bold")).place(x=220,y=350)
Radiobutton(frame,text="Absent",width = 10, variable=var,value=2,font=("arial",10,"bold")).place(x=100,y=350)
bt=Button(root,text="Attendance",width="10",bg="#023e8a",font=("times new roman",20,"bold"),command=add)
bt.place(x=90,y=440)
bt_1=Button(root,text="Record",bg="#023e8a",font=("times new roman",20,"bold"),command=show)
bt_1.place(x=270,y=440)
root.resizable(False,False)
root.mainloop()