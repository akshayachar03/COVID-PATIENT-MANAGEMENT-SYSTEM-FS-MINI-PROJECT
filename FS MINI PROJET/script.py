import sys
from tkinter import *
import os
import index
import datetime
from PIL import Image, ImageTk
from tkinter import messagebox


def clse():
    sys.exit()


def pos():
    ret = verifier()
    if ret == 0:
        h = open("admin.txt")
        lines = h.readlines()
        h.close()
        for i in lines:
            if i.find(eid.get()) != -1 and i.find(psw.get()) != -1:
                root.destroy()
                rec()
                os.system('python index.py')
                break
        else:
            messagebox.showwarning(
                "Warning", "Employee id or password is incorrect.")
    else:
        messagebox.showwarning("Warning", "Type Employee id and password.")


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


def rec():
    o = datetime.datetime.now()
    k = o.strftime("%Y:%m:%d | %H:%M:%S")
    rc = eid.get()+" | "+k
    g = open("record.txt", 'a')
    g.write(rc)
    g.close()


def im1():
    load = Image.open("img13.jpg")
    load = load.resize((350, 450), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render,background="black")
    img.image = render
    img.place(x=0, y=0)

    load1 = Image.open("img44.jpg")
    load1 = load1.resize((350, 450), Image.Resampling.LANCZOS)
    render1 = ImageTk.PhotoImage(load1)
    img1 = Label(root, image=render1,background="black")
    img1.image = render1
    img1.place(x=290, y=0)

    load1 = Image.open("img22.jpg")
    load1 = load1.resize((312, 450), Image.Resampling.LANCZOS)
    render1 = ImageTk.PhotoImage(load1)
    img1 = Label(root, image=render1,background="black")
    img1.image = render1
    img1.place(x=620, y=0)


if __name__ == "__main__":
    root = Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("COVID PATIENT MANAGEMENT SYSTEM")
    im1()
    eid = StringVar()
    psw = StringVar()
    label = Label(root, text="LOGIN", font="bold", fg="black",background="powder blue",width=22)
    label.place(x=350, y=65)
    label1 = Label(root, text="Employee id :",background='powder blue',width=12)
    label1.place(x=360, y=120)

    label2 = Label(root, text="Password      :",background='powder blue',width=12)
    label2.place(x=360, y=150)

    e1 = Entry(root, textvariable=eid,background='powder blue')
    e1.place(x=460, y=120)

    e2 = Entry(root, show='*', textvariable=psw,background='powder blue')
    e2.place(x=460, y=150)

    b4 = Button(root, text="Submit", command=pos,
                activebackground="Green",background="Cyan", width=30)
    b4.place(x=363, y=200)
    b3 = Button(root, text="Close", command=clse, bg="Red",
                activebackground="Blue", width=20)
    b3.place(x=780, y=420)
    root.mainloop()
