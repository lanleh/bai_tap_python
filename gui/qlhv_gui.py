import tkinter
from tkinter import *
from tkinter.ttk import *
import Connectsql

ketnoi = Connectsql.getConnection()
dulieu = ketnoi.cursor()

# Tạo giao diện
qlhv = tkinter.Tk()
qlhv.title = "Quản lý học viên"
qlhv.geometry("400x400")

# Tiêu đề
top = tkinter.Label(qlhv, text = "CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN", font=("Times New Roman","12")).grid(column = 2, row = 1)

#Tên
name = tkinter.Label(qlhv, text = "Name").grid(column = 1, row = 2)
giatri1 = tkinter.StringVar()
name_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri1).grid(column = 2, row = 2)

#Tuổi
age = tkinter.Label(qlhv, text = "Age").grid(column = 1, row = 3)
giatri2 = tkinter.IntVar()
age_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri2).grid(column = 2, row = 3)

#Quê
country = tkinter.Label(qlhv, text = "Country").grid(column = 1, row = 4)
giatri3 = tkinter.StringVar()
country_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri3).grid(column = 2, row = 4)

#Giới tính
sex = tkinter.Label(qlhv, text ="Sex").grid(column = 1, row = 5)
giatri6=StringVar()
sex_box = Combobox(qlhv, values = ["Male", "Female", "Unknown"], textvariable=giatri6)
sex_box.grid(column = 2, row =5)

#Điểm tin học
info = tkinter.Label(qlhv, text = "Information").grid(column = 1, row = 6)
giatri4 = tkinter.StringVar()
info_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri4).grid(column = 2, row = 6)

#Điểm tiếng Anh
eng = tkinter.Label(qlhv, text = "English").grid(column = 1, row = 7)
giatri5 = tkinter.StringVar()
eng_box = tkinter.Entry(qlhv, width = 25, textvariable = giatri5).grid(column = 2, row = 7)


# Thêm học viên

def themhocvien():
    dulieu.execute("INSERT INTO `Hocvien`(`Name`,Age,Country,Sex,English,Information) VALUES ('{}',{},'{}','{}',{},{})".format(giatri1.get(),giatri2.get(),giatri3.get(),giatri6.get(),float(giatri4.get()),float(giatri5.get())))
    ketnoi.commit()
    success1 = tkinter.Label(qlhv, text="Đã thêm").grid(column = 2, row = 8)
    success1.after(1000,success1.destroy)
    ketnoi.close()

them_hv = tkinter.Button(qlhv,text = "Thêm học viên",command = themhocvien).grid(column = 1, row = 8)





qlhv.mainloop()