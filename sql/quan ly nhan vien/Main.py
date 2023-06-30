from Quanlynhanvien import *

while True:
    print("Chuong trinh quan ly nhan vien")
    print("Menu \n 1. Hien thi nhan vien \n 2. Them nhan vien \n 3. Sua thong tin nhan vien \n 4. Xoa nhan vien \n 5. Xep loai theo luong \n 6. Xuat du lieu \n 0. Thoat")
    cau_lenh=int(input("Chon tac vu:"))
    if cau_lenh==1:
        display()
    elif cau_lenh==2:
        add()
        display()
    elif cau_lenh==3:
        update_data()
        display()
    elif cau_lenh==4:
        delete()
        display()
    elif cau_lenh==5:
        xeploailuong()
    elif cau_lenh==6:
        xuatdulieu()
    elif cau_lenh==0:
        a.close
        break
    else:
        print("ERROR")
