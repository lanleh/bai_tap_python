class PTTC1():
    def __init__(self,ten,tuoi,que_quan,lop,tieng_anh,tin_hoc):
        self.ten=ten
        self.tuoi=tuoi
        self.que_quan=que_quan
        self.lop=lop
        self.tieng_anh=tieng_anh
        self.tin_hoc=tin_hoc

PTTC1_list=[]
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
    PTTC1_list.append(hocvien)


print ("{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}".format("Ten","Tuoi","Que Quan","Lop","Tieng Anh","Tin Hoc"))
for i in PTTC1_list:
    print("{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}".format(i.ten,i.tuoi,i.que_quan,i.lop,i.tieng_anh,i.tin_hoc))
    
