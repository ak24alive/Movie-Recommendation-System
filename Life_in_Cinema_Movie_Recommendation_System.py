from Tkinter import *
from tkMessageBox import *
root=Tk()
root.title('Life in Cinema Movie Recommendation System')
import sqlite3
con=sqlite3.Connection("LifeinCinema_Database")
cur=con.cursor()
def About_Us():
    root1=Tk()
    root1.title('About Us')
    def funback():
        root1.destroy()
    Label(root1,text='About Us',width=35,height=3,font="Comic 10 bold").pack()
    Label(root1,text='We(or more precisely I) are a movie recommendation system. We recommend you movies according to the genre you prefer to watch.').pack()
    Label(root1,text='Life in Cinema Movie Recommendation system was founded by Akshat Khatri on 12/11/2016 as a part of his semester project. Since then it has helped a few people find the kind of movies they prefer to watch in their leisure time.').pack()
    Button(root1,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback,justify='right').pack()
def Contact_Us():
    root2=Tk()
    root2.title('Contact Us')
    def funback():
        root2.destroy()
    Label(root2,text='Contact Us',width=35,height=3,font="Comic 10 bold").pack()
    Label(root2,text='You can contact us on www.lifeincinema.com').pack()
    Label(root2,text='Contact Number: +918962286361, +919456435403, +917247368486').pack()
    Label(root2,text='Our Email Id are: akshatkhatri1@gmail.com, akshatkhatri2@gmail.com').pack()
    Button(root2,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback,justify='right').pack()
def HRM():
    root1=Tk()
    root1.title('Highest Rated Movies')
    Label(root1,text='').pack()
    Label(root1,text='').pack()
    con=sqlite3.Connection("LifeinCinema_Database")
    cur=con.cursor()
    def funback():
        root1.destroy()
    def Show_HRM():
        root=Tk()
        root.title('Highest Rated Movies')
        canvas = Canvas(root, borderwidth=0, background="#ffffff")
        frame = Frame(canvas, background="#ffffff")
        vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=frame, anchor="nw", 
                                  tags="frame")
        def onFrameConfigure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        frame.bind("<Configure>",onFrameConfigure)
        Label(frame,text='',bg='white').grid(row=0,column=0)
        Label(frame,text='',bg='white').grid(row=1,column=0)
        def data():
            Label(frame,text='Movie name').grid(row=2,column=0)
            Label(frame,text='Rating').grid(row=2,column=1)
            Label(frame,text="Director's Name").grid(row=2,column=2)
            j=3
            cur.execute("select * from Act where rating>=90 order by rating desc")
            m=cur.fetchall()
            for i in m:
                Label(frame,text=i[0],bg='white').grid(row=j,column=0)
                Label(frame,text=i[1],bg='white').grid(row=j,column=1)
                Label(frame,text=i[2],bg='white').grid(row=j,column=2)
                j=j+1
            cur.execute("select * from Rom where rating>=90 order by rating desc")
            m=cur.fetchall()
            for i in m:
                Label(frame,text=i[0],bg='white').grid(row=j,column=0)
                Label(frame,text=i[1],bg='white').grid(row=j,column=1)
                Label(frame,text=i[2],bg='white').grid(row=j,column=2)
                j=j+1
            cur.execute("select * from Com where rating>=90 order by rating desc")
            m=cur.fetchall()
            for i in m:
                Label(frame,text=i[0],bg='white').grid(row=j,column=0)
                Label(frame,text=i[1],bg='white').grid(row=j,column=1)
                Label(frame,text=i[2],bg='white').grid(row=j,column=2)
                j=j+1
            cur.execute("select * from Dra where rating>=90 order by rating desc")
            m=cur.fetchall()
            for i in m:
                Label(frame,text=i[0],bg='white').grid(row=j,column=0)
                Label(frame,text=i[1],bg='white').grid(row=j,column=1)
                Label(frame,text=i[2],bg='white').grid(row=j,column=2)
                j=j+1
            cur.execute("select * from Thr where rating>=90 order by rating desc")
            m=cur.fetchall()
            for i in m:
                Label(frame,text=i[0],bg='white').grid(row=j,column=0)
                Label(frame,text=i[1],bg='white').grid(row=j,column=1)
                Label(frame,text=i[2],bg='white').grid(row=j,column=2)
                j=j+1
            cur.execute("select * from Mys where rating>=90 order by rating desc")
            m=cur.fetchall()
            for i in m:
                Label(frame,text=i[0],bg='white').grid(row=j,column=0)
                Label(frame,text=i[1],bg='white').grid(row=j,column=1)
                Label(frame,text=i[2],bg='white').grid(row=j,column=2)
                j=j+1
            cur.execute("select * from Crm where rating>=90 order by rating desc")
            m=cur.fetchall()
            for i in m:
                Label(frame,text=i[0],bg='white').grid(row=j,column=0)
                Label(frame,text=i[1],bg='white').grid(row=j,column=1)
                Label(frame,text=i[2],bg='white').grid(row=j,column=2)
                j=j+1
        
        data()
        #root.geometry("500x500")
    Button(root1,text='Show Highest Rated Movies',width=30,height=2,font="Comic 10 bold",bg='Purple',command=Show_HRM).pack()
    Label(root1,text='').pack()
    Button(root1,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback).pack()

def Show_Act():
    root1=Tk()
    root1.title('Action Movies')
    con=sqlite3.Connection("LifeinCinema_Database")
    cur=con.cursor()
    def funback():
        root1.destroy()
    canvas = Canvas(root1, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root1, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", 
                                  tags="frame")
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>",onFrameConfigure)
    def data():
        cur.execute("select * from Act")
        m=cur.fetchall()
        Label(frame,text='',bg='white').grid(row=0,column=0)
        Label(frame,text='',bg='white').grid(row=1,column=0)
        Label(frame,text='The Action movies we recommend you are:',bg='white').grid(row=2,column=0)
        Label(frame,text='',bg='white').grid(row=3,column=0)
        Label(frame,text='Movie name').grid(row=4,column=0)
        Label(frame,text='Rating').grid(row=4,column=1)
        Label(frame,text="Director's Name").grid(row=4,column=2)
        j=5
        for i in m:
            Label(frame,text=i[0],bg='white').grid(row=j,column=0)
            Label(frame,text=i[1],bg='white').grid(row=j,column=1)
            Label(frame,text=i[2],bg='white').grid(row=j,column=2)
            j=j+1
        Label(frame,text='',bg='white').grid(row=j,column=0)
        Button(frame,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback).grid(row=j+1,column=0)
    data()
    #root.geometry("500x500")
def Show_Dra():
    root1=Tk()
    root1.title('Drama Movies')
    con=sqlite3.Connection("LifeinCinema_Database")
    cur=con.cursor()
    def funback():
        root1.destroy()
    canvas = Canvas(root1, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root1, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", 
                                  tags="frame")
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>",onFrameConfigure)
    def data():
        cur.execute("select * from Dra")
        m=cur.fetchall()
        Label(frame,text='',bg='white').grid(row=0,column=0)
        Label(frame,text='',bg='white').grid(row=1,column=0)
        Label(frame,text='The Drama movies we recommend you are:',bg='white').grid(row=2,column=0)
        Label(frame,text='',bg='white').grid(row=3,column=0)
        Label(frame,text='Movie name').grid(row=4,column=0)
        Label(frame,text='Rating').grid(row=4,column=1)
        Label(frame,text="Director's Name").grid(row=4,column=2)
        j=5
        for i in m:
            Label(frame,text=i[0],bg='white').grid(row=j,column=0)
            Label(frame,text=i[1],bg='white').grid(row=j,column=1)
            Label(frame,text=i[2],bg='white').grid(row=j,column=2)
            j=j+1
        Label(frame,text='',bg='white').grid(row=j,column=0)
        Button(frame,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback).grid(row=j+1,column=0)
    data()
    #root.geometry("500x500")

def Show_Crm():
    root1=Tk()
    root1.title('Crime Movies')
    con=sqlite3.Connection("LifeinCinema_Database")
    cur=con.cursor()
    def funback():
        root1.destroy()
    canvas = Canvas(root1, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root1, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", 
                                  tags="frame")
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>",onFrameConfigure)
    def data():
        cur.execute("select * from Crm")
        m=cur.fetchall()
        Label(frame,text='',bg='white').grid(row=0,column=0)
        Label(frame,text='',bg='white').grid(row=1,column=0)
        Label(frame,text='The Crime movies we recommend you are:',bg='white').grid(row=2,column=0)
        Label(frame,text='',bg='white').grid(row=3,column=0)
        Label(frame,text='Movie name').grid(row=4,column=0)
        Label(frame,text='Rating').grid(row=4,column=1)
        Label(frame,text="Director's Name").grid(row=4,column=2)
        j=5
        for i in m:
            Label(frame,text=i[0],bg='white').grid(row=j,column=0)
            Label(frame,text=i[1],bg='white').grid(row=j,column=1)
            Label(frame,text=i[2],bg='white').grid(row=j,column=2)
            j=j+1
        Label(frame,text='',bg='white').grid(row=j,column=0)
        Button(frame,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback).grid(row=j+1,column=0)
    data()
    #root.geometry("500x500")

def Show_Rom():
    root1=Tk()
    root1.title('Romantic Movies')
    con=sqlite3.Connection("LifeinCinema_Database")
    cur=con.cursor()
    def funback():
        root1.destroy()
    canvas = Canvas(root1, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root1, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", 
                                  tags="frame")
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>",onFrameConfigure)
    def data():
        cur.execute("select * from Rom")
        m=cur.fetchall()
        Label(frame,text='',bg='white').grid(row=0,column=0)
        Label(frame,text='',bg='white').grid(row=1,column=0)
        Label(frame,text='The Romantic movies we recommend you are:',bg='white').grid(row=2,column=0)
        Label(frame,text='',bg='white').grid(row=3,column=0)
        Label(frame,text='Movie name').grid(row=4,column=0)
        Label(frame,text='Rating').grid(row=4,column=1)
        Label(frame,text="Director's Name").grid(row=4,column=2)
        j=5
        for i in m:
            Label(frame,text=i[0],bg='white').grid(row=j,column=0)
            Label(frame,text=i[1],bg='white').grid(row=j,column=1)
            Label(frame,text=i[2],bg='white').grid(row=j,column=2)
            j=j+1
        Label(frame,text='',bg='white').grid(row=j,column=0)
        Button(frame,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback).grid(row=j+1,column=0)
    data()
    #root.geometry("500x500")

def Show_Com():
    root1=Tk()
    root1.title('Comedy Movies')
    con=sqlite3.Connection("LifeinCinema_Database")
    cur=con.cursor()
    def funback():
        root1.destroy()
    canvas = Canvas(root1, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root1, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", 
                                  tags="frame")
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>",onFrameConfigure)
    def data():
        cur.execute("select * from Com")
        m=cur.fetchall()
        Label(frame,text='',bg='white').grid(row=0,column=0)
        Label(frame,text='',bg='white').grid(row=1,column=0)
        Label(frame,text='The Comedy movies we recommend you are:',bg='white').grid(row=2,column=0)
        Label(frame,text='',bg='white').grid(row=3,column=0)
        Label(frame,text='Movie name').grid(row=4,column=0)
        Label(frame,text='Rating').grid(row=4,column=1)
        Label(frame,text="Director's Name").grid(row=4,column=2)
        j=5
        for i in m:
            Label(frame,text=i[0],bg='white').grid(row=j,column=0)
            Label(frame,text=i[1],bg='white').grid(row=j,column=1)
            Label(frame,text=i[2],bg='white').grid(row=j,column=2)
            j=j+1
        Label(frame,text='',bg='white').grid(row=j,column=0)
        Button(frame,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback).grid(row=j+1,column=0)
    data()
    #root.geometry("500x500")

def Show_Thr():
    root1=Tk()
    root1.title('Thriller Movies')
    con=sqlite3.Connection("LifeinCinema_Database")
    cur=con.cursor()
    def funback():
        root1.destroy()
    canvas = Canvas(root1, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root1, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", 
                                  tags="frame")
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>",onFrameConfigure)
    def data():
        cur.execute("select * from Thr")
        m=cur.fetchall()
        Label(frame,text='',bg='white').grid(row=0,column=0)
        Label(frame,text='',bg='white').grid(row=1,column=0)
        Label(frame,text='The Thriller movies we recommend you are:',bg='white').grid(row=2,column=0)
        Label(frame,text='',bg='white').grid(row=3,column=0)
        Label(frame,text='Movie name').grid(row=4,column=0)
        Label(frame,text='Rating').grid(row=4,column=1)
        Label(frame,text="Director's Name").grid(row=4,column=2)
        j=5
        for i in m:
            Label(frame,text=i[0],bg='white').grid(row=j,column=0)
            Label(frame,text=i[1],bg='white').grid(row=j,column=1)
            Label(frame,text=i[2],bg='white').grid(row=j,column=2)
            j=j+1
        Label(frame,text='',bg='white').grid(row=j,column=0)
        Button(frame,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback).grid(row=j+1,column=0)
    data()
    #root.geometry("500x500")

def Show_Mys():
    root1=Tk()
    root1.title('Mystery Movies')
    con=sqlite3.Connection("LifeinCinema_Database")
    cur=con.cursor()
    def funback():
        root1.destroy()
    canvas = Canvas(root1, borderwidth=0, background="#ffffff")
    frame = Frame(canvas, background="#ffffff")
    vsb = Scrollbar(root1, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw", 
                                  tags="frame")
    def onFrameConfigure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>",onFrameConfigure)
    def data():
        cur.execute("select * from Mys")
        m=cur.fetchall()
        Label(frame,text='',bg='white').grid(row=0,column=0)
        Label(frame,text='',bg='white').grid(row=1,column=0)
        Label(frame,text='The Mystery movies we recommend you are:',bg='white').grid(row=2,column=0)
        Label(frame,text='',bg='white').grid(row=3,column=0)
        Label(frame,text='Movie name').grid(row=4,column=0)
        Label(frame,text='Rating').grid(row=4,column=1)
        Label(frame,text="Director's Name").grid(row=4,column=2)
        j=5
        for i in m:
            Label(frame,text=i[0],bg='white').grid(row=j,column=0)
            Label(frame,text=i[1],bg='white').grid(row=j,column=1)
            Label(frame,text=i[2],bg='white').grid(row=j,column=2)
            j=j+1
        Label(frame,text='',bg='white').grid(row=j,column=0)
        Button(frame,text='Home',width=20,height=2,font="Comic 10 bold",bg='Brown',command=funback).grid(row=j+1,column=0)
    data()
    #root.geometry("500x500")

Button(root,text='About US',width=55,height=3,font="Comic 10 bold",fg='White',bg='Violet',command=About_Us,justify='right').grid(row=1,column=0)
Button(root,text='Contact US',width=55,height=3,font="Comic 10 bold",fg='White',bg='Violet',command=Contact_Us,justify='right').grid(row=1,column=1)
Button(root,text='Highest Rated Movies',width=57,height=3,font="Comic 10 bold",fg='White',bg='Violet',command=HRM,justify='right').grid(row=1,column=2)
joker_image=PhotoImage(file='Joker.gif')
label=Label(root,image=joker_image)
label.grid(row=2,column=0,columnspan=3,rowspan=16)
#Label(root,text='').grid(row=2,column=0)
Label(root,text='Choose the genre of which you want movie recommendation!!!',fg='white',bg='black').grid(row=3,column=0)
#Label(root,text='').grid(row=4,column=0)
Button(root,text='Action',width=20,height=2,font="Comic 10 bold",bg='White',command=Show_Act,justify='left').grid(row=5,column=0)
#Label(root,text='').grid(row=6,column=0)
Button(root,text='Drama',width=20,height=2,font="Comic 10 bold",bg='White',command=Show_Dra,justify='left').grid(row=7,column=0)
#Label(root,text='').grid(row=8,column=0)
Button(root,text='Mystery',width=20,height=2,font="Comic 10 bold",bg='White',command=Show_Mys,justify='left').grid(row=9,column=0)
#Label(root,text='').grid(row=10,column=0)
Button(root,text='Thriller',width=20,height=2,font="Comic 10 bold",bg='White',command=Show_Thr,justify='left').grid(row=11,column=0)
#Label(root,text='').grid(row=12,column=0)
Button(root,text='Romance',width=20,height=2,font="Comic 10 bold",bg='White',command=Show_Rom,justify='left').grid(row=13,column=0)
#Label(root,text='').grid(row=14,column=0)
Button(root,text='Comedy',width=20,height=2,font="Comic 10 bold",bg='White',command=Show_Com,justify='left').grid(row=15,column=0)
#Label(root,text='').grid(row=16,column=0)
Button(root,text='Crime',width=20,height=2,font="Comic 10 bold",bg='White',command=Show_Crm,justify='left').grid(row=17,column=0)
mainloop()

