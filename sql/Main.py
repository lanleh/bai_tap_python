from Quanlyhocvien import *

while True:

    print("Chuong trinh quan ly hoc vien \n Menu \n 1: Hien thi tat ca hoc vien \n 2: Hien thi hoc vien theo ID \n 3: Them hoc vien \n 4: Sua thong tin hoc vien \n 5: Xoa hoc vien \n 0: Thoat khoi chuong trinh")
    
    cau_lenh=int(input("Nhap so theo menu: "))
    
    if cau_lenh==1:
        getalldata()
    elif cau_lenh==2:
        data_theo_id()
    elif cau_lenh==3:
        createdata()
    elif cau_lenh==4:
        update_data()
    elif cau_lenh==5:
        xoa_data()
    elif cau_lenh==0:
        break
    else:
        print("Vui long nhap cac so tu 0 den 5")
