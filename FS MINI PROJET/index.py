from tkinter import *
import sys
import os
import datetime
from tkinter import font
from PIL import Image, ImageTk
import dele


def chpw():
    root.destroy()
    os.system('python chpw.py')


def verifier():
    a = b = c = d = e = f = 0
    if not name.get():
        t1.insert(END, "<>Name is required<>\n")
        a = 1
    if not adhar.get():
        t1.insert(END, "<>Adhar no is required<>\n")
        b = 1
    if not age.get():
        t1.insert(END, "<>Age is required<>\n")
        c = 1
    if not phone.get():
        t1.insert(END, "<>Phone number is requrired<>\n")
        d = 1
    if not cstatus.get():
        t1.insert(END, "<>Covid test result name is required<>\n")
        e = 1
    if not address.get():
        t1.insert(END, "<>Address is Required<>\n")
        f = 1
    if a == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1:
        return 1
    else:
        return 0


def ver():
    a = 0
    if not name.get():
        t1.insert(END, "<>Name is required<>\n")
        a = 1
    return a


def ser():
    t = ver()
    if (t == 0):
        f = open("positive.txt")
        lines = f.readlines()
        f.close()
        for i in lines:
            if i.find(name.get()) != -1:
                t1.insert(END, "\n"+i+"\n")
        g = open("negative.txt")
        lines1 = g.readlines()
        g.close()
        for j in lines1:
            if j.find(name.get()) != -1:
                t1.insert(END, "\n"+j+"\n")


def ad():
    ls = name.get()+'|'+adhar.get()+'|'+age.get()+'|'+phone.get() + \
        '|'+cstatus.get()+'|'+address.get()+"\n"
    if cstatus.get() == "positive":
        p = open('positive.txt', 'a')
        p.write(ls)
        p.close()
    if cstatus.get() == "negative":
        n = open('negative.txt', 'a')
        n.write(ls)
        n.close()


def add_patient():
    ret = verifier()
    if ret == 0:
        ad()
        t1.insert(END, "\nADDED SUCCESSFULLY\n")


def view_patient():
    p = open('positive.txt')
    n = open('negative.txt')
    c1 = p.read()
    c2 = n.read()
    p.close()
    n.close()
    t1.insert(END,"Name"+"|"+"Aadhar"+"|"+"Age"+"|"+"Phone Number"+"|"+"Covid19 result"+"|"+"Address"+"\t\t"+"\n")
    t1.insert(END, "\npositive"+"\n")
    t1.insert(END, c1)
    t1.insert(END, "\n"+"Negative"+"\n")
    t1.insert(END, c2)


def delete_patient():
    if not adhar.get():
        t1.insert(END, "<>Adhar is required<>\n")
    else:
        dele.pos(adhar.get())
        dele.neg(adhar.get())
        t1.insert(END, "\nDeleted successfully\n")


def update_patient():
    ret = verifier()
    if ret == 0:
        dele.pos(adhar.get())
        dele.neg(adhar.get())
        ad()
        t1.insert(END, "\nUpdated successfully\n")


def clse():
    rc()
    root.destroy()
    os.system('python script.py')


def add():
    root.destroy()
    os.system('python sinup.py')


def im():
    load = Image.open("img55.jpg")
    load = load.resize((285, 120), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=0, y=205)

def img():
    load = Image.open("img66.jpg")
    load = load.resize((640, 120), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render,background='powder blue')
    img.image = render
    img.place(x=290, y=310)




def rc():
    t = datetime.datetime.now()
    m = t.strftime("%Y:%m:%d - %H:%M:%S")
    rc = "   |   "+m+"\n"
    bg = open("record.txt", 'a')
    bg.write(rc)
    bg.close()


def rcp():
    p = open("record.txt")
    n = p.read()
    p.close()
    t1.insert(END, n)


if __name__ == "__main__":
    root = Tk()
    root.title("COVID PATIENT MANAGEMENT SYSTEM")
    root.minsize(930, 405)
    root.maxsize(935, 455)

    name = StringVar()
    adhar = StringVar()
    age = StringVar()
    phone = StringVar()
    cstatus = StringVar()
    address = StringVar()
    
    
    label1 = Label(root, text="Patient name:",background='powder blue',width=13)
    label1.place(x=0, y=0)

    label2 = Label(root, text="Adhar:",background='powder blue',width=13)
    label2.place(x=0, y=30)

    label3 = Label(root, text="Age:",background='powder blue',width=13)
    label3.place(x=0, y=60)

    label4 = Label(root, text="Phone Number:",background='powder blue',width=13)
    label4.place(x=0, y=90)

    label5 = Label(root, text="Covid19 test result:",background='powder blue',width=13)
    label5.place(x=0, y=120)

    label6 = Label(root, text="Address:",background='powder blue',width=13)
    label6.place(x=0, y=150)

    e1 = Entry(root, textvariable=name,background='powder blue',width=32)
    e1.place(x=100, y=0)

    e2 = Entry(root, textvariable=adhar,background='powder blue',width=32)
    e2.place(x=100, y=30)

    e3 = Entry(root, textvariable=age,background='powder blue',width=32)
    e3.place(x=100, y=60)

    e4 = Entry(root, textvariable=phone,background='powder blue',width=32)
    e4.place(x=100, y=90)

    e5 = Entry(root, textvariable=cstatus,background='powder blue',width=32)
    e5.place(x=100, y=120)

   

    e6 = Entry(root, textvariable=address,background='powder blue',width=32)
    e6.place(x=100, y=150)

    t1 = Text(root, width=80, height=20,background='RoyalBlue3',)
    t1.grid(row=10, column=1)

    def clearitem():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        

    b0 = Button(root, text="SEARCH", command=ser,background='royal blue',
                width=40, activebackground="green")
    b0.place(x=0, y=180)

    im()

    b1 = Button(root, text="ADD PATIENT", command=add_patient,background='royal blue',
                width=40, activebackground="green")
    b1.grid(row=11, column=0)

    b2 = Button(root, text="VIEW ALL PATIENTS",background='royal blue',
                command=view_patient, width=40, activebackground="green")
    b2.grid(row=12, column=0)

    b3 = Button(root, text="DELETE PATIENT", command=delete_patient,background='royal blue',
                width=40, activebackground="green")
    b3.grid(row=13, column=0)

    b4 = Button(root, text="UPDATE INFO", command=update_patient,background='royal blue',
                width=40, activebackground="green")
    b4.grid(row=14, column=0)

    b5 = Button(root, text="LOGOUT", command=clse,background='royal blue',
                width=40, activebackground="green")
    b5.grid(row=15, column=0)

#    b10=Button(root,text="Refresh screen",command=ref,activebackground="Green",width=25)
#    b10.place(x=590,y=405)

    b7 = Button(root, text="Change password",background='orange',
                activebackground="Green", command=chpw, width=25)
    b7.place(x=290, y=430)

    b9 = Button(root, text="Records", command=rcp,background='orange',
                activebackground="Green", width=25)
    b9.place(x=450, y=430)

    b6 = Button(root, text="Add Employee",background='orange',
                activebackground="Green", command=add, width=23)
    b6.place(x=619, y=430)

    b7= Button(root,  text="CLEAR", command=clearitem,background='orange',activebackground="RED",width=20)
    b7.place(x=785, y=430)
    img()

    root.mainloop()
