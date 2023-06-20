import import_sql

a=import_sql.getConnection()
data=a.cursor()

def display():
    data.execute("SELECT * FROM quan_ly_nhan_vien.nhanvien")
    output = data.fetchall()
    for i in output:
        print(i)

#    dem=[]
#    for i in output:
#        i=list(i)
#        id=int(input("Nhap ID can sua:"))
#        dem.append(i[4])
#        ID=i[4]+str(dem.count(i[4]))
#        data.execute("UPDATE quan_ly_nhan_vien.nhanvien SET ID = '{}' WHERE ID = {}".format(ID,id))
#        print(i)
        


def data_theo_id():
    n=input("Nhap ID:")
    data.execute("SELECT * FROM quan_ly_nhan_vien.nhanvien WHERE ID = {}".format(n))
    ketqua = data.fetchall()
    for i in ketqua:
        print(i)


def add():
    name=input("Nhap ten:")
    age=int(input("Nhap tuoi:"))
    country=input("Nhap que quan:")
    chucvu=input("Nhap chuc vu:")
    day=int(input("Nhap so ngay lam:"))
    sql= "INSERT INTO `Nhanvien`(`Name`, Age, Country, Chucvu, Songaylam) VALUES ('{}',{},'{}','{}',{})".format(name,age,country,chucvu,day)
    data.execute(sql)
    a.commit()

def update_data():
    id=int(input("Nhap ID cua du lieu can sua:"))
    print("Ban can sua thong tin gi? \n 1: Ten \n 2: Tuoi \n 3: Que quan \n 4: Chuc vu \n 5: So ngay lam")
    cau_lenh=int(input("Nhap 1,2,3,4:"))
    if cau_lenh==1:
        new_info=input("Nhap thong tin moi:")
        data.execute("UPDATE Quan_ly_nhan_vien.Nhanvien SET `Name` = '{}' WHERE ID = {}".format(new_info,id))
    elif cau_lenh==2:
        new_info=int(input("Nhap thong tin moi:"))
        data.execute("UPDATE Quan_ly_nhan_vien.Nhanvien SET Age = {} WHERE ID = {}".format(new_info,id))
    elif cau_lenh==3:
        new_info=input("Nhap thong tin moi:")
        data.execute("UPDATE Quan_ly_nhan_vien.Nhanvien SET Country = '{}' WHERE ID = {}".format(new_info,id))
    elif cau_lenh==4:
        new_info=input("Nhap thong tin moi:")
        data.execute("UPDATE Quan_ly_nhan_vien.Nhanvien SET Chucvu = {} WHERE ID = {}".format(new_info,id))
    elif cau_lenh==5:
        new_info=int(input("Nhap thong tin moi:"))
        data.execute("UPDATE Quan_ly_nhan_vien.Nhanvien SET Songaylam = {} WHERE ID = {}".format(new_info,id))
    a.commit()

def delete():
    id=int(input("Nhap ID cua du lieu can xoa:"))
    data.execute("DELETE FROM  Quan_ly_nhan_vien.Nhanvien WHERE ID = {}".format(id))
    a.commit()

add()