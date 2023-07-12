from import_sql import *
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *


ketnoi = getConnection()
dulieu = ketnoi.cursor()

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
title_box = Combobox(qlnv, values = ["NV", "TP", "GD"], textvariable=giatri4)
title_box.grid(column = 2, row = 5)

#Số ngày làm
workday = Label(qlnv, text = "Số ngày làm")
workday.grid(column = 1, row = 6)
giatri5 = IntVar()
workday_box = Entry(qlnv, width = 25, textvariable = giatri5)
workday_box.grid(column = 2, row = 6)

#Màn hình hiển thị
screen = ScrolledText(qlnv, width = 40, height = 10)
screen.grid(column = 2, row = 10)
screen['state'] = 'disabled'

#Kiểm tra kết nối
def kiemtraketnoi():
    test = ketnoi.is_connected()
    if test == True:
        success = Label(qlnv, text = "Connect Successful")
        success.grid(column = 2, row = 8)
        success.after(1000, success.destroy)
test_connection = Button(qlnv, text = "Kiểm tra kết nối", command = kiemtraketnoi)
test_connection.grid(column = 2, row = 11)

#Thêm nhân viên
def them():
    dulieu.execute("INSERT INTO `nhanvien`(`Name`,Age,Country,Chucvu,Songaylam) VALUES ('{}',{},'{}','{}',{})".format(giatri1.get(),giatri2.get(),giatri3.get(),giatri4.get(),giatri5.get()))
    ketnoi.commit()
    for giatri in (giatri1, giatri2, giatri3, giatri4, giatri5):
        giatri.set("")
    success = Label(qlnv, text = "Đã thêm")
    success.grid(column = 3, row = 9)
    success.after(1000, success.destroy)

nut_them = Button(qlnv, text = "Thêm nhân viên", command = them)
nut_them.grid(column =1, row = 7)


#Hiển thị nhân viên
def hienthi():
    screen['state'] = 'normal'
    dulieu.execute("SELECT * FROM quan_ly_nhan_vien.nhanvien")
    text = dulieu.fetchall()
    screen.insert("1.0", text)
    nutthaotac = Button(qlnv, text = "Xóa màn hình", command = lambda: [screen.delete("1.0", END), nutthaotac.destroy()])
    nutthaotac.grid(column = 3, row = 10)


nut_hien_thi = Button(qlnv, text = "Hiển thị nhân viên", command = hienthi)
nut_hien_thi.grid(column = 2, row = 7)


#Sửa nhân viên
def sua():
    sua1 = Label(qlnv, text="ID của nhân viên cần sửa")
    sua1.grid(column = 1, row = 10)
    id = IntVar()
    id_box = Entry(qlnv, width = 25, textvariable = id)
    id_box.grid(column = 2, row = 10)
    def thaotac():
        dulieu.execute("UPDATE quan_ly_nhan_vien.nhanvien SET `Name` = '{}', Age = {}, Country = '{}', Chucvu = '{}', Songaylam = {} WHERE ID = {}".format(giatri1.get(), giatri2.get(), giatri3.get(), giatri4.get(), giatri5.get(), id.get()))
        ketnoi.commit()
        success = Label(qlnv, text="Đã sửa")
        success.grid(column = 3, row =8)
        success.after(1000,success.destroy)
        sua1.after(1000,sua1.destroy)
        id_box.after(1100,id_box.destroy)
    nutthaotac1 = Button(qlnv, text = "Sửa", command = thaotac)
    nutthaotac1.grid(column = 3, row = 10)
    
sua_hv = Button(qlnv, text = "Sửa nhân viên", command = sua).grid(column = 2, row = 9)


#Xóa nhân viên
def xoa():
    xoa1 = Label(qlnv, text ="ID của nhân viên cần xóa")
    xoa1.grid(column = 1, row =10)
    id=IntVar()
    id_box = Entry(qlnv, width = 25, textvariable = id)
    id_box.grid(column  = 2, row = 10)
    def thaotac():
        dulieu.execute("DELETE from quan_ly_nhan_vien.nhanvien WHERE ID = {}".format(id.get()))
        ketnoi.commit()
        success = Label(qlnv, text = "Đã xóa")
        success.grid(column = 3, row = 8)
        success.after(1000, success.destroy)
        xoa1.after(1000, xoa1.destroy)
        id_box.after(1100, id_box.destroy)
    nutthaotac2 = Button(qlnv, text = "Xóa", command = thaotac)
    nutthaotac2.grid(column = 3, row = 10)

xoa_hv = Button(qlnv, text = "Xóa nhân viên", command = xoa).grid(column = 1, row = 9)



qlnv.mainloop()
ketnoi.close()