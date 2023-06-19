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
        print(i)

def data_theo_id():
    n=int(input("Nhap ID:"))
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien WHERE Id = {}".format(n))
    ketqua = dulieu.fetchall()
    for i in ketqua:
        print(i)

def getalldata2():
    dulieu.execute("SELECT * FROM quan_ly_hoc_vien.hocvien")
    ketqua = dulieu.fetchone()
    while ketqua is not None:
        print(ketqua)
        ketqua = dulieu.fetchone()

def createdata():
    dulieu.execute("INSERT INTO `Hocvien`(Id,`Name`,Age,Country,English,Information) VALUES ({},{},{},{},{},{})")
    ketnoi.commit
    print("Da them du lieu thanh cong")

# Lay du lieu to Mysql ve Visual Code
data_theo_id()

# Dong ket noi
ketnoi.close()