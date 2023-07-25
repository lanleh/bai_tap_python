from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import requests
import datetime

converter = Tk()
converter.title("Currency Converter")
converter.geometry("600x250")

label1 = Label(converter, text = "Amount").grid(column = 0, row = 0)
label2 = Label(converter, text = "USD Currency Converter Using Python").grid(column = 1, row = 0, columnspan = 2, sticky = E)

value1 = DoubleVar()
value_box1 = Entry(converter, width = 25, textvariable = value1).grid(column = 0, row = 1, columnspan = 2, padx = 10, pady = 5, sticky = W)

value2 = DoubleVar()
value_box2 = Entry(converter, width = 25, textvariable = value2).grid(column = 0, row = 2, columnspan = 2, padx = 10, pady = 5, sticky = W)

money = Image.open("API/bai 2/money.jpg")
mini_money = money.resize((50,50))
processed_image = ImageTk.PhotoImage(mini_money)
icon = Label(converter, image = processed_image).grid(column = 2, row = 1, rowspan = 2, padx = 10)

a = StringVar()
c1 = Combobox(converter, width = 20, textvariable = a)
c1.grid(column = 3, row = 1)

b = StringVar()
c2 = Combobox(converter, width = 20, textvariable = b)
c2.grid(column = 3, row = 2)


with open("API/bai 2/cl-currencies-table.txt","r") as read_file:
    content = read_file.readlines()

for line in content[:]:
    if "td" not in line:
        content.remove(line)
    else:
        new_content = [line.strip().removeprefix("<td>").removesuffix("</td>") for line in content]

currency_dict = {}
for i in new_content:
    if len(i) == 3:
        abbr = i
        name = content[content.index(i)+1]
        currency_dict[abbr] = name
 
c1["values"] = tuple(currency_dict.keys())
c2["values"] = tuple(currency_dict.keys())        


screen = Text(converter, width = 45, height = 5)
screen.grid(column = 1, row = 3, columnspan = 2, rowspan = 2, padx = 5)


def convert():
    currency_data = requests.get("http://api.currencylayer.com/live?access_key=4273d2c37f738367f08780b934ce7dda&format=1").json()
    currency1 = a.get()
    currency2 = b.get()
    currency_pair = currency1 + currency2
    try:
        if "USD" in currency_pair:
            if "USD" == currency_pair[:3]:
                price = currency_data["quotes"][currency_pair]
            else:
                flipped = currency2 + currency1
                price = 1/(currency_data["quotes"][flipped])
        else:
            ratio1 = currency_data["quotes"]["USD"+currency2]
            ratio2 = currency_data["quotes"]["USD"+currency1]
            price = ratio1/ratio2
        m = value1.get()
        n = value2.get()
        try:
            if n/m != price:
                value2.set(round(m*price, 2))
        except ZeroDivisionError:
                value1.set(round(1/price*n, 2))
        screen.insert(END, "{} {} equals {} {}".format(value1.get(), currency_dict[currency1], value2.get(), currency_dict[currency2]))
        screen.insert(END,"\nLast Time Update --- {}".format(datetime.datetime.fromtimestamp(currency_data["timestamp"])))
    except:
        screen.insert(END, "N/A")

def erase():
    screen.delete("1.0", END)
    value1.set(0)
    value2.set(0)

search = Button(converter, text = "Search", command = convert).grid(column = 0, row = 3)
eraser = Button(converter, text = "Clear", command = erase).grid(column = 0, row = 4)

converter.mainloop()