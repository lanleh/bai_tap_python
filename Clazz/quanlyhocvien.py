from PTTC1 import PTTC1

class Quanlyhocvien:
    PTTC1_list=[]
    def themhocvien(self):
        n=int(input("Nhap so luong hoc vien:"))
        for i in range(n):
            print("Nhap hoc vien thu {}".format(i+1))
            ten = input("Nhap ten:")
            try:
                tuoi = int(input("Nhap tuoi:"))
            except:
                print("error")
            que_quan=input("Nhap que quan:")
            lop=input("Nhap lop:")
            try:
                tieng_anh=float(input("Nhap diem tieng Anh:"))
            except:
                print("error")
            try:
                tin_hoc=float(input("Nhap diem Tin hoc:"))
            except:
                print("error")
            hocvien=PTTC1(ten,tuoi,que_quan,lop,tieng_anh,tin_hoc)
            diemtrungbinh=(tieng_anh+tin_hoc)/2
            if diemtrungbinh>5:
                hocvien.xeploai="Gioi"
            else:
                hocvien.xeploai="Yeu"
            hocvien.id=i+1
            self.PTTC1_list.append(hocvien)

    def hienthihocvien(self):
        print ("{:<15}{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}{:<20}".format("ID","Ten","Tuoi","Que Quan","Lop","Tieng Anh","Tin Hoc","Xep Loai"))
        for i in self.PTTC1_list:
            print("{:<15}{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}{:<20}".format(i.id,i.ten,i.tuoi,i.que_quan,i.lop,i.tieng_anh,i.tin_hoc,i.xeploai)
                  
    def suathongtin(self,hocvien_id):
    for hocvien in self.PTTC1_list:
        if hocvien_id==hocvien.id:
            tenmoi=input("Thay ten hoc vien:")
            hocvien.ten=tenmoi
            try:
                tuoimoi=input(int("Thay tuoi hoc vien:"))
            except:
                print("error")
            hocvien.tuoi=tuoimoi
            self.hienthihocvien
                  
   def xoa_hoc_vien(self,hocvien_id):
        for hocvien in self.PTTC1_list:
            if hocvien_id == hocvien.id:
                self.PTTC1_list.pop(hocvien_id-1)
                self.hienthihocvien()               

test=Quanlyhocvien()
test.themhocvien()
test.hienthihocvien()
