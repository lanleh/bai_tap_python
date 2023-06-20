import Connectsql


# Ket noi voi MySQL
ketnoi = Connectsql.getConnection()
#print(ketnoi)

dulieu = ketnoi.cursor()

def getalldata():
    # yeu cau mysql thuc hien cau lenh trong ngoac kep
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    # Trả du lieu
    ketqua = dulieu.fetchall()
    for i in ketqua:
        i=list(i)
        diem_trung_binh = (i[4]+i[5])/2
        if diem_trung_binh > 5:
            xeploai = "Gioi"
        else:
            xeploai = "Yeu"
        i.append(xeploai)
        print(i)

def data_theo_id():
    n=int(input("Nhap ID:"))
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien WHERE Id = {}".format(n))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        i=list(i)
        diem_trung_binh = (i[4]+i[5])/2
        if diem_trung_binh > 5:
            xeploai = "Gioi"
        else:
            xeploai = "Yeu"
        i.append(xeploai)
        print(i)
        
def getalldata2():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchone()
    while ketqua is not None:
        print(ketqua)
        ketqua = dulieu.fetchone()

def createdata():
    print("Them du lieu")
    id=int(input("Nhap id:"))
    name=input("Nhap ten:")
    age=int(input("Nhap tuoi:"))
    country=input("Nhap que quan:")
    english=int(input("Nhap diem tieng Anh:"))
    info=int(input("Nhap diem tin hoc:"))
    sql= "INSERT INTO `Hocvien`(Id,`Name`,Age,Country,English,Information) VALUES ({},'{}',{},'{}',{},{})".format(id,name,age,country,english,info)
    dulieu.execute(sql)
    ketnoi.commit()


def update_data():
    id=int(input("Nhap ID cua du lieu can sua:"))
    print("Ban can sua thong tin gi? \n 1: Ten \n 2: Tuoi \n 3: Que quan \n 4: Diem tieng Anh \n 5: Diem tin hoc")
    cau_lenh=int(input("Nhap 1,2,3,4:"))
    if cau_lenh==1:
        new_info=input("Nhap thong tin moi:")
        dulieu.execute("UPDATE Quan_ly_hoc_vien.Hocvien SET `Name` = '{}' WHERE Id = {}".format(new_info,id))
    elif cau_lenh==2:
        new_info=int(input("Nhap thong tin moi:"))
        dulieu.execute("UPDATE Quan_ly_hoc_vien.Hocvien SET Age = {} WHERE Id = {}".format(new_info,id))
    elif cau_lenh==3:
        new_info=input("Nhap thong tin moi:")
        dulieu.execute("UPDATE Quan_ly_hoc_vien.Hocvien SET Country = '{}' WHERE Id = {}".format(new_info,id))
    elif cau_lenh==4:
        new_info=int(input("Nhap thong tin moi:"))
        dulieu.execute("UPDATE Quan_ly_hoc_vien.Hocvien SET English = {} WHERE Id = {}".format(new_info,id))
    elif cau_lenh==5:
        new_info=int(input("Nhap thong tin moi:"))
        dulieu.execute("UPDATE Quan_ly_hoc_vien.Hocvien SET Information = {} WHERE Id = {}".format(new_info,id))
    ketnoi.commit()

def xoa_data():
    id=int(input("Nhap ID cua du lieu can xoa:"))
    dulieu.execute("DELETE FROM  Quan_ly_hoc_vien.Hocvien WHERE Id = {}".format(id))
    ketnoi.commit()


# Dong ket noi
# ketnoi.close()