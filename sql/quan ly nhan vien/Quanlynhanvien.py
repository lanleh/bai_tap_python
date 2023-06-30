import import_sql

a=import_sql.getConnection()
data=a.cursor()

def new_id_n_luong():
    data.execute("SELECT * FROM quan_ly_nhan_vien.nhanvien")
    output = data.fetchall()
    dem=[]
    for i in output:
        # Tao ID moi
        dem.append(i[4])
        ID=i[4]+str(dem.count(i[4]))
        # Hien thi chuc vu va tinh luong
        if i[4]=='NV':
            chucvu="Nhan vien"
            luong=300000*i[5]*1
        elif i[4]=='TP':
            chucvu="Truong phong"
            luong=300000*i[5]*1.6
        elif i[4]=='GD':
            chucvu="Giam doc"
            luong=300000*i[5]*2
        # Thay doi gia tri trong output    
        j=list(i)
        j[0]=ID
        j[4]=chucvu
        j.append(luong)
        output[output.index(i)]=j
    return(output)

def display():
    print ("{:<15}{:<15}{:<15} {:<15} {:<15} {:<15}".format("ID","Ten","Tuoi","Que quan","Chuc vu","Luong"))
    new_list=new_id_n_luong()
    for i in new_list:
        print ("{:<15}{:<15}{:<15} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4],i[6]))        



def data_theo_id():
    new_list=new_id_n_luong()
    id=input("Nhap ID cua nhan vien:")
    for i in new_list:
        if i[0] == id:
           print ("{:<15}{:<15}{:<15} {:<15} {:<15} {:<15}".format("ID","Ten","Tuoi","Que quan","Chuc vu","Luong"))
           print ("{:<15}{:<15}{:<15} {:<15} {:<15} {:<15}".format(i[0],i[1],i[2],i[3],i[4],i[6]))
#    data.execute("SELECT * FROM quan_ly_nhan_vien.nhanvien WHERE ID = {}".format(n))
#    ketqua = data.fetchall()
#    for i in ketqua:
#        print(i)



def add():
    name=input("Nhap ten:")
    age=int(input("Nhap tuoi:"))
    country=input("Nhap que quan:")
    while True:
        a=input("Nhap chuc vu:")
        if a in ("NV", "TP", "GD"):
            chucvu=a
            break
        else:
            print("Vui long nhap NV, TP, GD: ")
    day=int(input("Nhap so ngay lam:"))
    sql= "INSERT INTO `Nhanvien`(`Name`, Age, Country, Chucvu, Songaylam) VALUES ('{}',{},'{}','{}',{})".format(name,age,country,chucvu,day)
    data.execute(sql)
    a.commit()
    



def update_data():
    id=int(input("Nhap so thu tu cua nhan vien can sua:"))
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
    id=int(input("Nhap so thu tu cua nhan vien can xoa:"))
    data.execute("DELETE FROM  Quan_ly_nhan_vien.Nhanvien WHERE ID = {}".format(id))
    a.commit()


def xeploailuong():
    new_list=new_id_n_luong()
    new_list.sort(key=lambda x: x[6],reverse=True)
    print ("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format("ID","Ten","Tuoi","Que quan","Chuc vu","Luong"))
    for i in new_list:
        print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i[0],i[1],i[2],i[3],i[4],i[6]))


def xuatdulieu():
    text = new_id_n_luong()
    b = open("sql/quan ly nhan vien/dulieu.txt","w")
    b.write("{:<15}{:<15}{:<15} {:<15} {:<15} {:<15}\n".format("ID","Ten","Tuoi","Que quan","Chuc vu","Luong"))
    for i in text:
        nhanvien="{:<15}{:<15}{:<15} {:<15} {:<15} {:<15}\n".format(i[0],i[1],i[2],i[3],i[4],i[6])
        b.write(nhanvien)
    b.close()