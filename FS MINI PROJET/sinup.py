from tkinter import *
import os
import sys
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import messagebox

from numpy import size


def back():
    root.destroy()
    os.system('python index.py')


def verifier():
    a = b = 0
    if not eid.get():
        a = 1
    if not psw.get():
        b = 1
    if a == 1 or b == 1:
        return 1
    else:
        return 0


def add():
    ret = verifier()
    if ret == 0:
        la = eid.get()+' | '+psw.get()+"\n"
        f = open("admin.txt", "a")
        f.write(la)
        f.close()
        os.system('python index.py')

def img2():
    load = Image.open('covid 19.jpg')
    load = load.resize((931,450), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(load) 
    img = Label(root, image=render,anchor=CENTER,background='red')
    img.image = render
    img.place(x=0, y=0)            


if __name__ == "__main__":
    root = Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.configure(bg="gray25")
    root.title("COVID PATIENT MANAGEMENT SYSTEM")
    img2()

    eid = StringVar()
    psw = StringVar()
    label = Label(root, text="ADD EMPLOYEE", font="bold", fg="white",width=40,background="black")
    label.place(x=310, y=60)
    label1 = Label(root, text="Employee id        :",fg="white",background="black")
    label1.place(x=360, y=120)

    label2 = Label(root,text="Create Password :",fg="white",background="black")
    label2.place(x=360, y=150)

    e1 = Entry(root, textvariable=eid,background="black",fg="white")
    e1.place(x=460, y=120)

    e2 = Entry(root,show='*', textvariable=psw,background="black",fg="white")
    e2.place(x=460, y=150)

    b4 = Button(root, text="Submit", command=add, bg="#ff0000",background="white",
                activebackground="Green", width=30)
    b4.place(x=363, y=200)

    b3 = Button(root, text="Back", command=back, bg="Black",fg="white",
                activebackground="white", width=20)
    b3.place(x=750, y=420)
    root.mainloop()
