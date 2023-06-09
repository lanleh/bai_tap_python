n=int(input("Nhap so luong diem:"))
r=float(input("Nhap ban kinh duong tron:"))
tap_hop=[]
for i in range (1,n+1):
    diem=[]
    x=float(input("Nhap x:"))
    diem.append(x)
    y=float(input("Nhap y:"))
    diem.append(y)
    tap_hop.append(diem)
dem_so=0
for diem in tap_hop:
    d=(diem[0]**2+diem[1]**2)**0.5
    if d<r:
       dem_so+=1
    else:
        continue
print("Co {} diem nam trong duong tron".format(dem_so))
