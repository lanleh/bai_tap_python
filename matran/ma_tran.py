m=int(input("Nhap so cot cua ma tran:"))
n=int(input("Nhap so hang cua ma tran:"))
ma_tran=[]
def nhap():
    for i in range(1,m+1):
        hang=[]
        for j in range(1,n+1):
            phan_tu=int(input("Nhap phan tu thu {} cua hang {}:".format(j,i)))
            hang.append(phan_tu)
        ma_tran.append(hang)


def xuat():
    for a in range(len(ma_tran)):
        hang=str()
        for b in range(len(ma_tran[a])):
            hang+=str(ma_tran[a][b])+"   "
        print(hang)

def output():
    for a in range(len(ma_tran)):
        for b in range(len(ma_tran[a])):
            print("{:<10}".format(ma_tran[a][b]),end="")
        print()

nhap()
output()