from quanlynhanvien import *
test = quanlynhanvien()
while True:
    print("|--------------------------------------|")
    print("|----Chuong trinh quan ly nhan vien    |")
    print("|1. Chuc nang them                     |")
    print("|2. Chuc nang xoa                      |")
    print("|3. Chuc nang sua                      |")
    print("|4. Chuc nang hien thi                 |")
    print("|0. Thoat                              |")
    print("|--------------------------------------|")

    nhap = int(input("Nhap chuc nang theo so: "))
    if nhap == 1:
        print("------------------")
        test.themnhanvien()
    elif nhap == 2:
        test.xoanhanvien()
    elif nhap == 3:
        test.suathongtin()
    elif nhap == 4:
        test.hienthinhanvien()
    elif nhap == 0:
        print("Tam biet")
        break
    else: 
        print("Nhap sai vui long nhap lai")
