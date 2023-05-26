#Digital Clock Using Python with GUI

from re import I
from tkinter import *

import datetime

def date_time():
    time=datetime.datetime.now()
    hour=time.strftime('%I')
    min=time.strftime('%M')
    sec=time.strftime('%S')
    am=time.strftime('%p')
    date=time.strftime('%d')
    mon=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')

    lab_hour.config(text=hour)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mon.config(text=mon)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hour.after(200,date_time)


clock=Tk()
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.config(bg="pink")

#********TIME********
lab_hour=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg="brown",fg="white")
lab_hour.place(x=120,y=50,height=110,width=100)
lab_hour_txt=Label(clock,text="Hour",font=('Times New Roman',20,"bold"),bg="brown",fg="white")
lab_hour_txt.place(x=120,y=190,height=30,width=100)

lab_min=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg="brown",fg="white")
lab_min.place(x=340,y=50,height=110,width=100)
lab_min_txt=Label(clock,text="Minutes",font=('Times New Roman',20,"bold"),bg="brown",fg="white")
lab_min_txt.place(x=340,y=190,height=30,width=100)

lab_sec=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg="brown",fg="white")
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_txt=Label(clock,text="Seconds",font=('Times New Roman',20,"bold"),bg="brown",fg="white")
lab_sec_txt.place(x=560,y=190,height=30,width=100)

lab_am=Label(clock,text="00",font=('Times New Roman',40,"bold"),bg="brown",fg="white")
lab_am.place(x=780,y=50,height=110,width=100)
lab_am_txt=Label(clock,text="AM/PM",font=('Times New Roman',20,"bold"),bg="brown",fg="white")
lab_am_txt.place(x=780,y=190,height=30,width=100)

#*******DATE********
lab_date=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg="brown",fg="white")
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_txt=Label(clock,text="Date",font=('Times New Roman',20,"bold"),bg="brown",fg="white")
lab_date_txt.place(x=120,y=410,height=30,width=100)

lab_mon=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg="brown",fg="white")
lab_mon.place(x=340,y=270,height=110,width=100)
lab_mon_txt=Label(clock,text="Month",font=('Times New Roman',20,"bold"),bg="brown",fg="white")
lab_mon_txt.place(x=340,y=410,height=30,width=100)

lab_year=Label(clock,text="00",font=('Times New Roman',60,"bold"),bg="brown",fg="white")
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_txt=Label(clock,text="Year",font=('Times New Roman',20,"bold"),bg="brown",fg="white")
lab_year_txt.place(x=560,y=410,height=30,width=100)

lab_day=Label(clock,text="00",font=('Times New Roman',40,"bold"),bg="brown",fg="white")
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_txt=Label(clock,text="Day",font=('Times New Roman',20,"bold"),bg="brown",fg="white")
lab_day_txt.place(x=780,y=410,height=30,width=100)

date_time()

clock.mainloop()
