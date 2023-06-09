import math
class Diem:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def nam_trong(self, ban_kinh):
        khoang_cach=math.sqrt(self.x**2+self.y**2)
        if khoang_cach<=ban_kinh:
            return True
        else:
            return False

n=int(input("So diem muon nhap:"))
list_diem=[]
for i in range(1,n+1):
    x=float(input("nhap x:"))
    y=float(input("Nhap y:"))
    toa_do=Diem(x,y)
    list_diem.append(toa_do)

ban_kinh=float(input("Nhap ban kinh:"))
so_diem=0
for toa_do in list_diem:
    if toa_do.nam_trong(ban_kinh):
        so_diem+=1
print("So diem nam trong duong tron la {}".format(so_diem))