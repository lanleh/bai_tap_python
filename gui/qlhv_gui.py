import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *

import Connectsql

ketnoi = Connectsql.getConnection()
dulieu = ketnoi.cursor()


# Tạo giao diện
qlhv = Tk()
qlhv.title = "Quản lý học viên"
qlhv.geometry("500x400")

# Tiêu đề
top = Label(qlhv, text = "CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN", font=("Times New Roman","12")).grid(column = 2, row = 1)

#Tên
name = Label(qlhv, text = "Name").grid(column = 1, row = 2)
giatri1 = StringVar()
name_box = Entry(qlhv, width = 25, textvariable = giatri1).grid(column = 2, row = 2)

#Tuổi
age = Label(qlhv, text = "Age").grid(column = 1, row = 3)
giatri2 = IntVar()
age_box = Entry(qlhv, width = 25, textvariable = giatri2).grid(column = 2, row = 3)

#Quê
country = Label(qlhv, text = "Country").grid(column = 1, row = 4)
giatri3 = StringVar()
country_box = Entry(qlhv, width = 25, textvariable = giatri3).grid(column = 2, row = 4)

#Giới tính
sex = Label(qlhv, text ="Sex").grid(column = 1, row = 5)
giatri6=StringVar()
sex_box = Combobox(qlhv, values = ["Male", "Female", "Unknown"], textvariable=giatri6).grid(column = 2, row =5)

#Điểm tin học
info = Label(qlhv, text = "Information").grid(column = 1, row = 6)
giatri4 = DoubleVar()
info_box = Entry(qlhv, width = 25, textvariable = giatri4).grid(column = 2, row = 6)

#Điểm tiếng Anh
eng = Label(qlhv, text = "English").grid(column = 1, row = 7)
giatri5 = DoubleVar()
eng_box = Entry(qlhv, width = 25, textvariable = giatri5).grid(column = 2, row = 7)

#Màn hình hiển thị
thongtinhv = StringVar()
scrolled = ScrolledText(qlhv,width= 25, height = 10).grid(column=2,row=10)


# Thêm học viên
def themhocvien():
    dulieu.execute("INSERT INTO `Hocvien`(`Name`,Age,Country,Sex,Information,English) VALUES ('{}',{},'{}','{}',{},{})".format(giatri1.get(),giatri2.get(),giatri3.get(),giatri6.get(),giatri4.get(),giatri5.get()))
    ketnoi.commit()
    success1 = Label(qlhv, text="Đã thêm").grid(column = 2, row = 8)
    for box in (name_box, age_box, country_box, sex_box, info_box, eng_box):
        box.clear("1.0", END)
    success1.after(1000, success1.destroy())
    ketnoi.close()

them_hv = Button(qlhv,text = "Thêm học viên",command = themhocvien).grid(column = 1, row = 8)


#Hiển thị học viên
def hienthi():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien_2.hocvien")
    text = dulieu.fetchall()
    scrolled.insert(INSERT, text)
    ketnoi.close()

hienthi_hv = Button(qlhv, text = "Hiển thị học viên", command = hienthi).grid(column = 2, row = 8)


#Sửa học viên
def sua():
    sua1 = Label(qlhv, text="ID của học viên cần sửa").grid(column = 1, row = 10)
    id = IntVar()
    id_box = Entry(qlhv, width = 25, textvariable = id).grid(column = 2, row = 10)
    def thaotac():
        dulieu.execute("SELECT * FROM quan_ly_hoc_vien_2.hocvien")
        danh_sach = dulieu.fetchall()
        for i in range(len(danh_sach)):
            if id == danh_sach[i][0]:
                print("yes")
            else:
                print("no")
                #dulieu.execute("UPDATE quan_ly_hoc_vien_2.hocvien SET `Name` = '{}', Age = {}, Country = '{}', Sex = '{}', Information = {} and English = {} WHERE ID = {}".format(giatri1.get(),giatri2.get(),giatri3.get(),giatri6.get(),giatri4.get(),giatri5.get(),id))     
                #ketnoi.commit()
                #ketnoi.close()
    nutthaotac = Button(qlhv, text = "Sửa", command = thaotac).grid(column = 3, row = 10)
    

sua_hv = Button(qlhv, text = "Sửa học viên", command = sua).grid(column = 1, row = 9)




qlhv.mainloop()