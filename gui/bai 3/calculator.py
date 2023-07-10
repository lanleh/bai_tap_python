from tkinter import *
from tkinter.ttk import *

calc = Tk()
calc.title("Calculator")
calc.geometry("400x350")


input = StringVar()

def erase():
    input.set("")

erase()

eraser = Button(calc, text="C", command = erase)
eraser.grid(column = 2, row = 0)


for i in range(9,0,-1):
    a = Button(calc, text=str(i))
    if i%3 == 0:
        a.grid(column = 0, row = int(i/3))
    elif i%3 == 2:
        a.grid(column = 1, row = int((i+1)/3))
    else:
        a.grid(column = 2, row = int((i+2)/3))
 

#nine = Button(calc, text="9", command = lambda: input.set(9)).grid(column=0, row=1)



input_box = Entry(calc, width = 25, textvariable = input)
input_box.grid(column = 1, row = 0)










calc.mainloop()
