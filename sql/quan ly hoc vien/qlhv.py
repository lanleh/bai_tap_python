import tkinter
from tkinter import *

qlhv = tkinter.Tk()
qlhv.title = "Quản lý học viên"
qlhv.geometry("400x400")

top = tkinter.Label(qlhv, text = "CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN", font=("Times New Roman","12")).grid(column = 2, row = 1)

name = tkinter.Label(qlhv, text = "Name").grid(column = 1, row = 2)
name = tkinter.Entry(qlhv, width = 25).grid(column = 2, row = 2)

age = tkinter.Label(qlhv, text = "Age").grid(column = 1, row = 3)
age = tkinter.Entry(qlhv, width = 25).grid(column = 2, row = 3)

country = tkinter.Label(qlhv, text = "Country").grid(column = 1, row = 4)
country = tkinter.Entry(qlhv, width = 25).grid(column = 2, row = 4)

sex = tkinter.Label(qlhv, text ="Sex").grid(column = 1, row = 5)
sex = tkinter.Entry(qlhv, width = 25).grid(column = 2, row = 5)

info = tkinter.Label(qlhv, text = "Information").grid(column = 1, row = 6)
info = tkinter.Entry(qlhv, width = 25).grid(column = 2, row = 6)

eng = tkinter.Label(qlhv, text = "English").grid(column = 1, row = 7)
eng = tkinter.Entry(qlhv, width = 25).grid(column = 2, row = 7)



qlhv.mainloop()