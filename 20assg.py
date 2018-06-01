"""database insert delete and update by the rajkumar any problem contect use fb.com/raj0kumar00"""
from __future__ import print_function
import Tkinter
from tkinter import *
import MySQLdb as my
db = my.connect(host="localhost",user="root",passwd="123456",db="python" ) #change host username password and dbname
top=Tkinter.Tk()
top.title('database management')
top.geometry('500x400')
def exit():
    global top
    top.destroy()
def dataso():#data show when button clicked
    db = my.connect(host="localhost",user="root",passwd="123456",db="python")#change host username password and dbname
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM student""")
    data=cursor.fetchall()
    np=Label(top, text="total submited users..!!!")
    np.pack()
    for row in data:
        f1=Label(top, text=row[0])
        f1.pack(side=LEFT)
    db.close()
def hide1():# use for hide the buttons
    ins.pack_forget()
    upd.pack_forget()
    delt.pack_forget()
def hide2():#use for hide buttons in to the main window
    L1.pack_forget()
    E1.pack_forget()
    L2.pack_forget()
    E2.pack_forget()
    L3.pack_forget()
    E3.pack_forget()
    subm.pack_forget()
def submit():
    global cursor
    cursor=db.cursor()
    nm=E1.get()
    rl=E2.get()
    cl=E3.get()
    sql = "insert into student VALUES('%s', '%s', '%s')" % \
    (nm, rl, cl)
    cursor.execute(sql)
    db.commit()
    db.close()
    hide2()
    notise=Label(top, text="Your details is submited....!!!")
    notise.pack()
    dataso()
    exit()
def insert():
    global E1,E2,E3,L1,L2,L3,subm
    hide1()
    L1=Label(top, text="Name")
    L1.pack(side=TOP)
    E1=Entry(top, bd=5)
    E1.focus()
    E1.pack(side=TOP)
    L2=Label(top, text="role num")
    L2.pack(side=TOP)
    E2=Entry(top, bd=5)
    E1.focus()
    E2.pack(side=TOP)
    L3=Label(top, text="collage")
    L3.pack(side=TOP)
    E3=Entry(top, bd=5)
    E1.focus()
    E3.pack(side=TOP)
    subm=Tkinter.Button(top,text="Submit",command=submit)
    subm.pack()
def upda():
    global cursor
    cursor = db.cursor()
    usnm=username.get()
    newnm=o1.get()
    newrole=o2.get()
    newcolla=o3.get()
    sql="UPDATE student set name = '%s', role_num='%s', collage='%s' where name= '%s'" % \
    (newnm, newrole,newcolla,usnm)
    cursor.execute(sql)
    db.commit()
    db.close()
    hide2()
    notise=Label(top, text="Your details is submited....!!!")
    notise.pack()
    exit()
def update():
    global p1,o1,p2,o2,p3,o3,submi,username
    hide1()
    dataso()
    upnot=Label(top, text="Enter the user name to update")
    upnot.pack(side=TOP)
    username=Entry(top, bd=5)
    username.pack(side=TOP)
    hide1()
    p1=Label(top, text="Name")
    p1.pack(side=TOP)
    o1=Entry(top, bd=5)
    o1.focus()
    o1.pack(side=TOP)
    p2=Label(top, text="role num")
    p2.pack(side=TOP)
    o2=Entry(top, bd=5)
    o1.focus()
    o2.pack(side=TOP)
    p3=Label(top, text="collage")
    p3.pack(side=TOP)
    o3=Entry(top, bd=5)
    o1.focus()
    o3.pack(side=TOP)
    submi=Tkinter.Button(top,text="Submit",command=upda)
    submi.pack()
def delpak():
    global cursor
    cursor = db.cursor()
    pkchu=usernamed.get()
    sql="DELETE from student where name ='%s'" %\
    (pkchu)
    cursor.execute(sql)
    db.commit()
    db.close()
    exit()
def delete():
    global usernamed
    hide1()
    dataso()
    upna=Label(top, text="Enter the user name to delete")
    upna.pack(side=TOP)
    usernamed=Entry(top, bd=5)
    usernamed.focus()
    usernamed.pack(side=TOP)
    delp=Tkinter.Button(top,text="Submit",command=delpak)
    delp.pack()
    hide1()
#main window start
ins=Tkinter.Button(top, text="Insert",command=insert)
ins.pack()
upd=Tkinter.Button(top, text="Update", command=update)
upd.pack()
delt=Tkinter.Button(top, text="Delete", command=delete)
delt.pack()
top.mainloop()
#main window end 
#thankyou 
#fb.com/rajkumar
