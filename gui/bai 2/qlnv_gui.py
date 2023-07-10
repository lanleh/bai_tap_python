from import_sql import *
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *


ketnoi = getConnection()
dulieu = ketnoi.cursor

# Tạo giao diện
qlnv = Tk()
qlnv.title = "Quản lý nhân viên"
qlnv.geometry("575x425")

# Tiêu đề
top = Label(qlnv, text = "CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN", font=("Times New Roman","12"))
top.grid(column = 2, row = 1)

#Tên
name = Label(qlnv, text = "Tên")
name.grid(column = 1, row = 2)
giatri1 = StringVar()
name_box = Entry(qlnv, width = 25, textvariable = giatri1)
name_box.grid(column = 2, row = 2)

#Tuổi
age = Label(qlnv, text = "Tuổi")
age.grid(column = 1, row = 3)
giatri2 = IntVar()
age_box = Entry(qlnv, width = 25, textvariable = giatri2)
age_box.grid(column = 2, row = 3)

#Quê
country = Label(qlnv, text = "Quê quán")
country.grid(column = 1, row = 4)
giatri3 = StringVar()
country_box = Entry(qlnv, width = 25, textvariable = giatri3)
country_box.grid(column = 2, row = 4)

#Chức vụ
title = Label(qlnv, text = "Chức vụ")
title.grid(column = 1, row = 5)
giatri4 = StringVar()
title_box = Entry(qlnv, width = 35, textvariable = giatri4)

#Số ngày làm
workday = Label(qlnv, text = "Số ngày làm")
workday.grid(column = 1, row = 6)
giatri5 = IntVar()
workday_box = Entry(qlnv, width = 25, textvariable = giatri5)

