from coban import *
from Nangcao.nangcao import *

a=int(input("Nhap so a:"))
b=int(input("Nhap so b:"))

print(tong(a,b))
print(hieu(a,b))
print(tich(a,b))
try:
    print(thuong(a,b))
except(ZeroDivisionError):
    print("khong the chia cho 0")

m=int(input("Nhap so m:"))
print(can_bac_hai(m))
print(binh_phuong(m))