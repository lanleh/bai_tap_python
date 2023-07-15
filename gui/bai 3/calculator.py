from tkinter import *
from tkinter.ttk import *

calc = Tk()
calc.title("Calculator")
calc.geometry("400x350")


input = StringVar()
input_box = Entry(calc, width = 25, textvariable = input)
input_box.grid(column = 1, row = 0)


def click(a):
    global output
    output = ""
    if a == "%":
        output = str(int(input.get())/100)
        input.set(output)
    else:
        output = output + str(a)
    input.set(output)

#Số
nine = Button(calc, text="9", command = lambda: click(9)).grid(column=0, row=1)
eight = Button(calc, text = "8", command = lambda: click(8)).grid(column = 1, row = 1)
seven = Button(calc, text = "7", command = lambda: click(7)).grid(column = 2, row = 1)
six = Button(calc, text = "6", command = lambda: click(6)).grid(column = 0, row = 2)
five = Button(calc, text = "5", command = lambda: click(5)).grid(column = 1, row = 2)
four = Button(calc, text = "4", command = lambda: click(4)).grid(column = 2, row = 2)
three = Button(calc, text = "3", command = lambda: click(3)).grid(column = 0, row = 3)
two = Button(calc, text = "2", command = lambda: click(2)).grid(column = 1, row = 3)
one = Button(calc, text = "1", command = lambda: click(1)).grid(column = 2, row = 3)
zero = Button(calc, text = "0", command = lambda: click(0)).grid(column = 0, row = 4)
double_zero = Button(calc, text = "00", command = lambda: click("00")).grid(column = 1, row = 4)

#Phép tính
dot = Button(calc, text=".", command = lambda: click(".")).grid(column = 2, row =4)
plus = Button(calc, text="+", command = lambda: click("+")).grid(column = 3, row = 1)
minus = Button(calc, text="-", command = lambda: click("-")).grid(column = 3, row = 2)
mult = Button(calc, text="*", command = lambda: click("*")).grid(column =3, row = 3)
div = Button(calc, text = "/", command = lambda: click("/")).grid(column = 3, row = 4)
percent = Button(calc, text = "%", command = lambda: click("%")).grid(column = 2, row = 5)

#Kết quả
def res():
    a = eval(input.get())
    input.set(a)

result = Button(calc, text = "Result", command = res).grid()


#Nút xóa
eraser = Button(calc, text="C", command = lambda: input.set("")).grid(column = 3, row = 0)



calc.mainloop()
