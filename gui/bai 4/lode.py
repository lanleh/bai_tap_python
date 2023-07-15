from tkinter import *
from tkinter.scrolledtext import *
import random


lode = Tk()
lode.title("Tro choi lo de")
lode.geometry("800x500")


top = Label(lode, text = "Trò chơi Lô Đề", font = ("Times New Roman", "14")).grid(row = 0, column = 2)

choilo = Label(lode, text = "I. Chơi Lô"). grid(row = 1, column = 0)
chonso1 = Label(lode, text = "Chọn số").grid(row = 2, column = 0)
so_lo = IntVar()
box1 = Entry(lode, width = 25, textvariable = so_lo).grid(row = 2, column = 1)
danhmaydiem1 = Label(lode, text = "Đánh mấy điểm:").grid(row = 2, column = 2)
diem_lo = IntVar()
box2 = Entry(lode, width = 25, textvariable = diem_lo).grid(row = 2, column = 3)
note1 = Label(lode, text = "1 điểm = 23.000 VNĐ").grid(row = 4, column = 3)

choide = Label(lode, text = "II. Chơi Đề").grid(row = 5, column = 0)
chonso2 = Label(lode, text = "Chọn số").grid(row = 6, column = 0)
so_de = IntVar()
box3 = Entry(lode, width = 25, textvariable = so_de).grid(row = 6, column = 1)
danhmaydiem2 = Label(lode, text = "Đánh mấy điểm:").grid(row = 6, column = 2)
diem_de = IntVar()
box4 = Entry(lode, width = 25, textvariable = diem_de).grid(row = 6, column = 3)
note2 = Label(lode, text = "1 điểm = 1.000 VNĐ").grid(row = 8, column = 3)

screen = ScrolledText(width = 35, height = 10)
screen.grid(row = 9, column = 2)

tongtien = Label(lode, text = "Tổng tiền: 1.000.000 VNĐ").grid(row = 10, column = 0)
note3 = Label(lode, text = "Số tiền còn lại:").grid(row = 11, column = 0)


tien = IntVar()
tien.set(1000000)
sotienconlai = Entry(lode, width = 10, textvariable = tien).grid(row = 11, column = 1)

def ketqua(game):
    def quayso(n):
        if n < 4:
            a = random.randint(1,99999)
            return((5-len(str(a)))*"0"+str(a))
        elif n in (4,5):
            a = random.randint(1,9999)
            return((4-len(str(a)))*"0"+str(a))
        elif n == 6:
            a = random.randint(1,999)
            return((3-len(str(a)))*"0"+str(a))
        elif n == 7:
            a = random.randint(1,99)
            return((2-len(str(a)))*"0"+str(a))
        
    winners = []    

    def giai(n, soluong):
        for i in range(soluong):    
            b = quayso(n)
            winner = int(b[-2:])
            winners.append(winner)
            screen.insert(END,b+" ") 

    def tinhtien(game):
        reward = 0
        if game == "lo":
            bet = so_lo.get()
            c = winners.count(bet)
            if c != 0:
                reward = c*diem_lo.get()*23000
            else:
                reward = -diem_lo.get()*23000
        elif game == "de":
            bet = so_de.get()
            c = winners.count(bet)
            if c!=0:
                reward = c*diem_de.get()*1000
            else:
                reward = -diem_de.get()*1000
        outcome = tien.get() + reward
        if outcome <= 0:
            outcome = 0
            screen.delete("1.0", END)
            screen.insert(END, "ĐÃ HẾT TIỀN")
        tien.set(outcome)

    screen.delete("1.0",END)
    screen.insert(END,"Giải ĐB: ")
    giai(0,1)
    screen.insert(END,"\n1: ")
    giai(1,1)
    screen.insert(END,"\n2: ")
    giai(2,2)
    screen.insert(END,"\n3: ")
    giai(3,3)
    screen.insert(END,"\n")
    giai(3,3)
    screen.insert(END, "\n4: ")
    giai(4,4)
    screen.insert(END, "\n5: ")
    giai(5,3)
    screen.insert(END,"\n")
    giai(5,3)
    screen.insert(END,"\n6: ")
    giai(6,3)
    screen.insert(END,"\n7: ")
    giai(7,4)
    
    tinhtien(game)

play1 = Button(lode, text = "Chơi đi đừng sợ", command = lambda: ketqua("lo")).grid(row = 3, column = 2)
play2 = Button(lode, text = "Chơi đi đừng sợ", command = lambda: ketqua("de")).grid(row = 7, column = 2)


mainloop()