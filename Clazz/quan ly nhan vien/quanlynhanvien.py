class nv():
    def __init__(self,ten,tuoi,que_quan,chamcong):
        self.ten=ten
        self.tuoi=tuoi
        self.que_quan=que_quan
        self.chamcong=chamcong

class quanlynhanvien:
    list_nhanvien=[]
    def themnhanvien(self):
        self.soluong=[]
        n=int(input("Nhap so luong nhan vien:"))
        for i in range(n):
            print("Nhap nhan vien thu {}".format(i+1))
            ten=input("Nhap ten:")
            tuoi=int(input("Nhap tuoi:"))
            que_quan=input("Nhap que quan:")
            chamcong=int(input("So ngay cong:"))
            nhanvien=nv(ten,tuoi,que_quan,chamcong)
            machucvu=input("Nhap chuc vu (NV,TP,GD):")
            if machucvu=="TP":
                nhanvien.chucvu="Truong phong"
                heso=1.6
            elif machucvu=="NV":
                nhanvien.chucvu="Nhan vien"
                heso=1
            elif machucvu=="GD":
                nhanvien.chucvu="Giam doc"
                heso=2
            else:
                break
            nhanvien.luong=int(300000*chamcong*heso)
            self.soluong.append(machucvu)
            nhanvien.id=str(machucvu+str(self.soluong.count(machucvu)))
            self.list_nhanvien.append(nhanvien)
    

    def hienthinhanvien(self):
        print ("{:<15}{:<15}{:<15} {:<15} {:<15} {:<15}".format("ID","Ten","Tuoi","Que Quan","Chuc Vu","Luong"))
        for i in self.list_nhanvien:
            print("{:<15}{:<15}{:<15} {:<15} {:<15} {:<15}".format(i.id,i.ten,i.tuoi,i.que_quan,i.chucvu,i.luong))

    def suathongtin(self):
        nhanvien_id=input("Nhap ma nhan vien can sua:")
        for nhanvien in self.list_nhanvien:
            if nhanvien_id==nhanvien.id:
                tenmoi=input("Nhap ten moi:")
                nhanvien.ten=tenmoi
                tuoimoi=int(input("Nhap tuoi moi:"))
                nhanvien.tuoi=tuoimoi
    
    def xoanhanvien(self):
        nhanvien_id=input("Nhap ma nhan vien can xoa:")
        for nhanvien in self.list_nhanvien:
            if nhanvien_id==nhanvien.id:
                self.list_nhanvien.remove(nhanvien)

