from tkinter import *
import os
import sys
from tkinter import messagebox
from turtle import color
from PIL import Image, ImageTk
from cv2 import blur


def back():
    root.destroy()
    os.system('python index.py')



def verifier():
    a = b = c = 0
    if not eid.get():
        a = 1
    if not psw1.get():
        b = 1
    if not psw.get():
        c = 1
    if a == 1 or b == 1 or c == 1:
        return 1
    else:
        return 0

def im():
    load = Image.open('covid.gif')
    load = load.resize((931,450), Image.Resampling.LANCZOS)
    render = ImageTk.PhotoImage(load) 
    img = Label(root, image=render,anchor=CENTER,background='orange')
    img.image = render
    img.place(x=0, y=0)


def update():
    ret = verifier()
    if ret == 0:
        la = eid.get()+' | '+psw.get()+"\n"
        a = open("admin.txt")
        lines = a.readlines()
        a.close()
        p = -1
        q = 0
        r = -1
        for i in lines:
            q = q+1
            p = i.find(eid.get())
            r = i.find(psw1.get())
            if p != -1 and r != -1:
                flag = 1
                break
        if p != -1 and r != -1:
            del lines[q-1]
            b = open("admin.txt", "w+")
            for line in lines:
                b.write(line)
            b.close()
            f = open("admin.txt", "a")
            f.write(la)
            f.close()
            messagebox.showinfo("Information", "Password changed.")
            root.destroy()
            os.system('python index.py')

    else:
        messagebox.showwarning(
            "Warning", "Type Employee id,current and new passwords.")


if __name__ == "__main__":
    root = Tk()
    root.minsize(935, 455)
    root.maxsize(935, 455)
    root.title("COVID PATIENT MANAGEMENT SYSTEM")
    im()

    eid = StringVar()
    psw = StringVar()
    psw1 = StringVar()
    label = Label(root, text="CHANGE PASSWORD", font="bold", fg="green")
    label.place(x=380, y=50)
    label1 = Label(root, text="Employee id :")
    label1.place(x=360, y=120)

    label2 = Label(root, text="Current Password :")
    label2.place(x=360, y=150)

    label2 = Label(root, text="New Password :")
    label2.place(x=360, y=180)

    e1 = Entry(root, textvariable=eid)
    e1.place(x=470, y=120)

    e2 = Entry(root,show='*', textvariable=psw1)
    e2.place(x=470, y=150)

    e3 = Entry(root,show='*', textvariable=psw)
    e3.place(x=470, y=180)

    b4 = Button(root, text="Submit", command=update, bg="Green",
                activebackground="#ff0000", width=30)
    b4.place(x=365, y=210)

    b3 = Button(root, text="Cancel", command=back, bg="red",fg='white',
                activebackground="Green", width=20)
    b3.place(x=780, y=420)
    root.mainloop()
