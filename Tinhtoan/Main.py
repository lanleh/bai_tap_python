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

n=int(input("Nhap so n:"))
print(can_bac_hai(n))
print(binh_phuong(n))