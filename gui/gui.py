import tkinter

giaodien = tkinter.Tk()
giaodien.title("Chuong trinh")
giaodien.geometry("500x200")

label3 = tkinter.Label(giaodien,text="Tinh tong 2 so",fg="black",bg="white")
label3.grid(column=3, row=0)

label1 = tkinter.Label(giaodien,text="So thu nhat",fg="black",bg="white")
label1.grid(column=2,row=1)
giatri1 = tkinter.IntVar()
textbox1 = tkinter.Entry(giaodien,width=30,textvariable=giatri1)
textbox1.grid(column=3,row=1)


label2 = tkinter.Label(giaodien,text="So thu hai",fg="black",bg="white")
label2.grid(column=2,row=2)
giatri2=tkinter.IntVar()
textbox2 = tkinter.Entry(giaodien,width=30,textvariable=giatri2)
textbox2.grid(column=3, row=2)


def cong():
    tong = giatri1.get() + giatri2.get()
    giatri3.set(tong)
def tru():
    hieu = giatri1.get() - giatri2.get()   
    giatri3.set(hieu)
def nhan():
    tich = giatri1.get() * giatri2.get()
    giatri3.set(tich)
def chia():
    thuong = giatri1.get() / giatri2.get()
    giatri3.set(thuong)

sum = tkinter.Button(giaodien, text="Cong",fg="black",bg="yellow",command=cong)
sum.grid(column=4, row=3)

minus = tkinter.Button(giaodien, text="Tru", fg="black",bg="yellow",command=tru)
minus.grid(column=5,row=3)

multi = tkinter.Button(giaodien, text="Nhan",fg="black",bg="yellow",command=nhan)
multi.grid(column=6,row=3)

div = tkinter.Button(giaodien, text="Chia",fg="black",bg="yellow",command=chia)
div.grid(column=7,row=3)

giatri3 = tkinter.IntVar()
textbox3 = tkinter.Entry(giaodien,width=10,textvariable=giatri3)
textbox3.grid(column=3,row=6)



giaodien.mainloop()