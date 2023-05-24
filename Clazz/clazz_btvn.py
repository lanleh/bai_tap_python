class PTTC1():
    def __init__(self,ten,tuoi,que_quan,lop,tieng_anh,tin_hoc):
        self.ten=ten
        self.tuoi=tuoi
        self.que_quan=que_quan
        self.lop=lop
        self.tieng_anh=tieng_anh
        self.tin_hoc=tin_hoc
PTTC1_list=[]
student1=PTTC1("A",22,"Ha Noi","A",5,5)
PTTC1_list.append(student1)
student2=PTTC1("B",23,"HCM","A",5.5,6)
PTTC1_list.append(student2)
student3=PTTC1("D",34,"Da Nang","A",6,6)
PTTC1_list.append(student3)
print ("{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}".format("Ten","Tuoi","Que Quan","Lop","Tieng Anh","Tin Hoc"))
for i in PTTC1_list:
    print("{:<15} {:<15} {:<15} {:<10}{:<15}{:<20}".format(i.ten,i.tuoi,i.que_quan,i.lop,i.tieng_anh,i.tin_hoc))
    
