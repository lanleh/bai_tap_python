import tkinter
from tkinter import *
from tkinter.ttk import *
import Connectsql

ketnoi = Connectsql.getConnection()
dulieu = ketnoi.cursor()


qlhv = tkinter.Tk()
qlhv.title = "Quản lý học viên"
qlhv.geometry("400x400")

top = tkinter.Label(qlhv, text = "CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN", font=("Times New Roman","12")).grid(column = 2, row = 1)

name = tkinter.Label(qlhv, text = "Name").grid(column = 1, row = 2)
giatri1 = tkinter.StringVar()
name_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri1).grid(column = 2, row = 2)


age = tkinter.Label(qlhv, text = "Age").grid(column = 1, row = 3)
giatri2 = tkinter.IntVar()
age_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri2).grid(column = 2, row = 3)


country = tkinter.Label(qlhv, text = "Country").grid(column = 1, row = 4)
giatri3 = tkinter.StringVar()
country_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri3).grid(column = 2, row = 4)


sex = tkinter.Label(qlhv, text ="Sex").grid(column = 1, row = 5)
sex_box = Combobox(qlhv)
sex_box['values'] = ("Male", "Female", "Unknown")
sex_box.grid(column = 2, row =5)
giatri6

info = tkinter.Label(qlhv, text = "Information").grid(column = 1, row = 6)
giatri4 = tkinter.IntVar()
info_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri4).grid(column = 2, row = 6)


eng = tkinter.Label(qlhv, text = "English").grid(column = 1, row = 7)
giatri5 = tkinter.IntVar()
eng_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri5).grid(column = 2, row = 7)


them_hv = tkinter.Button(qlhv,text = "Thêm học viên").grid(column = 1, row = 8)
def themhocvien():
    dulieu.execute("INSERT INTO `Hocvien`(`Name`,Age,Country,Sex,English,Information) VALUES ({'{}',{},'{}','{}',{},{})".format(giatri1.get(),giatri2.get(),giatri3.get(),giatri6,giatri4.get(),giatri5.get()))






qlhv.mainloop()