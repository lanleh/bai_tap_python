import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *

import Connectsql

ketnoi = Connectsql.getConnection()
dulieu = ketnoi.cursor()


# Tạo giao diện
qlhv = Tk()
qlhv.title("Quản lý học viên")
qlhv.geometry("575x425")

# Tiêu đề
top = Label(qlhv, text = "CHƯƠNG TRÌNH QUẢN LÝ HỌC VIÊN", font=("Times New Roman","12"))
top.grid(column = 2, row = 1)

#Tên
name = Label(qlhv, text = "Name")
name.grid(column = 1, row = 2)
giatri1 = StringVar()
name_box = Entry(qlhv, width = 25, textvariable = giatri1)
name_box.grid(column = 2, row = 2)

#Tuổi
age = Label(qlhv, text = "Age")
age.grid(column = 1, row = 3)
giatri2 = IntVar()
age_box = Entry(qlhv, width = 25, textvariable = giatri2)
age_box.grid(column = 2, row = 3)

#Quê
country = Label(qlhv, text = "Country")
country.grid(column = 1, row = 4)
giatri3 = StringVar()
country_box = Entry(qlhv, width = 25, textvariable = giatri3)
country_box.grid(column = 2, row = 4)

#Giới tính
sex = Label(qlhv, text ="Sex")
sex.grid(column = 1, row = 5)
giatri6=StringVar()
sex_box = Combobox(qlhv, values = ["Male", "Female", "Unknown"], textvariable=giatri6)
sex_box.grid(column = 2, row =5)

#Điểm tin học
info = Label(qlhv, text = "Information")
info.grid(column = 1, row = 6)
giatri4 = DoubleVar()
info_box = Entry(qlhv, width = 25, textvariable = giatri4)
info_box.grid(column = 2, row = 6)

#Điểm tiếng Anh
eng = Label(qlhv, text = "English")
eng.grid(column = 1, row = 7)
giatri5 = DoubleVar()
eng_box = Entry(qlhv, width = 25, textvariable = giatri5)
eng_box.grid(column = 2, row = 7)

#Màn hình hiển thị
screen = ScrolledText(qlhv,width= 40, height = 10)
screen.grid(column=2,row=10)
screen['state'] = 'disabled'

#Kiểm tra kết nối
def test_connection():
    if ketnoi.is_connected() == True:
        success = Label(qlhv, text = "Connect Successful")
        success.grid(column=2, row=12)
        success.after(1000, success.destroy)

test_button = Button(qlhv, text = "Kiểm tra kết nối", command = test_connection)
test_button.grid(column=2, row=11)


# Thêm học viên
def themhocvien():
    dulieu.execute("INSERT INTO `Hocvien`(`Name`,Age,Country,Sex,Information,English) VALUES ('{}',{},'{}','{}',{},{})".format(giatri1.get(),giatri2.get(),giatri3.get(),giatri6.get(),giatri4.get(),giatri5.get()))
    ketnoi.commit()
    success = Label(qlhv, text="Đã thêm")
    success.grid(column = 3, row = 8)
    success.after(1500, success.destroy)
    for giatri in (giatri1, giatri2, giatri3, giatri4, giatri5, giatri6):
        giatri.set("")

them_hv = Button(qlhv,text = "Thêm học viên",command = themhocvien).grid(column = 1, row = 8)


#Hiển thị học viên
def hienthi():
    screen['state'] = 'normal'
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien_2.hocvien")
    text = dulieu.fetchall()
    screen.insert("1.0",text)
    nutthaotac = Button(qlhv, text = "Xóa màn hình", command = lambda: [screen.delete("1.0", END), nutthaotac.destroy()])
    nutthaotac.grid(column = 3, row = 10)

hienthi_hv = Button(qlhv, text = "Hiển thị học viên", command = hienthi).grid(column = 2, row = 8)


#Sửa học viên
def sua():
    sua1 = Label(qlhv, text="ID của học viên cần sửa")
    sua1.grid(column = 1, row = 10)
    id = IntVar()
    id_box = Entry(qlhv, width = 25, textvariable = id)
    id_box.grid(column = 2, row = 10)
    def thaotac():
        dulieu.execute("UPDATE quan_ly_hoc_vien_2.hocvien SET `Name` = '{}', Age = {}, Country = '{}', Sex = '{}', Information = {} and English = {} WHERE ID = {}".format(giatri1.get(),giatri2.get(),giatri3.get(),giatri6.get(),giatri4.get(),giatri5.get(),id.get()))     
        ketnoi.commit()
        for giatri in (giatri1, giatri2, giatri3, giatri4, giatri5, giatri6):
            giatri.set("")
        success = Label(qlhv, text="Đã sửa")
        success.grid(column = 3, row =8)
        success.after(1000,success.destroy)
        sua1.after(1000,sua1.destroy)
        id_box.after(1100,id_box.destroy)
    nutthaotac = Button(qlhv, text = "Sửa", command = lambda: [thaotac(), nutthaotac.destroy()])
    nutthaotac.grid(column = 3, row = 10)
    
sua_hv = Button(qlhv, text = "Sửa học viên", command = sua).grid(column = 2, row = 9)


#Xóa học viên
def xoa():
    xoa1 = Label(qlhv, text="ID của học viên cần xóa")
    xoa1.grid(column = 1, row = 10)
    id = IntVar()
    id_box = Entry(qlhv, width = 25, textvariable = id)
    id_box.grid(column = 2, row = 10)
    def thaotac():
        dulieu.execute("DELETE FROM quan_ly_hoc_vien_2.hocvien WHERE ID = {}".format(id.get()))    
        ketnoi.commit()        
        success = Label(qlhv, text="Đã xóa")
        success.grid(column = 3, row =8)
        success.after(1000,success.destroy)
        xoa1.after(1000,xoa1.destroy)
        id_box.after(1100,id_box.destroy)
    nutthaotac = Button(qlhv, text = "Xóa", command = lambda: [thaotac(), nutthaotac.destroy()])
    nutthaotac.grid(column = 3, row = 10)  

xoa_hv = Button(qlhv, text="Xóa học viên", command = xoa).grid(column = 1, row = 9)




qlhv.mainloop()
ketnoi.close()