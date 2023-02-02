import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)

    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['RegNo'])
    e2.insert(0, select['First_Name'])
    e3.insert(0, select['Last_Name'])
    e4.insert(0, select['Fname'])
    e5.insert(0, select['DOB'])
    e6.insert(0, select['Gender'])
    e7.insert(0, select['Contact'])
    e8.insert(0, select['Address'])


def Add():
    RegNo= e1.get()
    First_Name= e2.get()
    Last_Name = e3.get()
    Fname = e4.get()
    DOB = e5.get()
    Gender = e6.get()
    Contact = e7.get()
    Address = e8.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  registation (RegNo,First_Name,Last_Name,Fname,DOB,Gender,Contact,Address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (RegNo,First_Name,Last_Name,Fname,DOB,Gender,Contact,Address)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("INSERT TABLE", "Student Data Inserted Successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    RegNo = e1.get()
    First_Name = e2.get()
    Last_Name = e3.get()
    Fname = e4.get()
    DOB = e5.get()
    Gender = e6.get()
    Contact = e7.get()
    Address = e8.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  registation set  First_Name= %s,Last_Name= %s,Fname= %s,DOB= %s,Gender= %s,Contact= %s,Address= %s where RegNo= %s"
        val = (First_Name,Last_Name,Fname,DOB,Gender,Contact,Address,RegNo)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("UPDATE TABLE", "Student Data Updated Successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    RegNo = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from registation where RegNo = %s"
        val = (RegNo,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("RECORD TABLE", "Student Data Deleted successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e7.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="management")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT RegNo,First_Name,Last_Name,Fname,DOB,Gender,Contact,Address FROM registation")
    records = mycursor.fetchall()
    print(records)

    for i, (RegNo,First_Name,Last_Name,Fname,DOB,Gender,Contact,Address) in enumerate(records, start=1):
        listBox.insert("", "end", values=(RegNo,First_Name,Last_Name,Fname,DOB,Gender,Contact,Address))
        mysqldb.close()


root = Tk()
root.title("Student Registration Form")
root.geometry("900x580")
root.configure(bg='lightblue')
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8

tk.Label(root,bg='lightblue', text="Student Registation", fg="blue", font=("Algerian", 30)).place(x=250, y=5)

tk.Label(root,bg='lightblue', text="Registration No").place(x=10, y=60)
Label(root,bg='lightblue', text="Student Name").place(x=10, y=90)
Label(root,bg='lightblue', text="Father Name").place(x=10, y=120)
Label(root,bg='lightblue', text="Date of Birth").place(x=10, y=150)
Label(root,bg='lightblue', text="Gender").place(x=10, y=180)
Label(root,bg='lightblue', text="Contact").place(x=10, y=210)
Label(root,bg='lightblue', text="Address").place(x=10, y=240)


e1 = Entry(root)
e1.place(x=140, y=60)

e2 = Entry(root)
e2.place(x=140, y=90)

e3 = Entry(root)
e3.place(x=140, y=120)

e4 = Entry(root)
e4.place(x=140, y=150)

e5 = Entry(root)
e5.place(x=140, y=180)

e6 = Entry(root)
e6.place(x=140, y=210)

e7 = Entry(root)
e7.place(x=140, y=240)

Button(root, text="ADD", command=Add, height=3, width=13).place(x=255, y=280)
Button(root, text="UPDATE", command=update, height=3, width=13).place(x=365, y=280)
Button(root, text="DELETE", command=delete, height=3, width=13).place(x=475, y=280)

cols = ('RegNo','Name','Fname','DOB','Gender','Contact','Address')

listBox = ttk.Treeview(root, columns=cols, show='headings')
listBox.column('RegNo', width=50, anchor=CENTER)
listBox.column('Name', width=140, anchor=CENTER)
listBox.column('Fname', width=140, anchor=CENTER)
listBox.column('DOB', width=140, anchor=CENTER)
listBox.column('Gender', width=140, anchor=CENTER)
listBox.column('Contact', width=140, anchor=CENTER)
listBox.column('Address', width=143, anchor=CENTER)

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=0, column=0, columnspan=2)
    listBox.place(x=2, y=350)

show()
listBox.bind('<Double-Button-1>', GetValue)
root.mainloop()