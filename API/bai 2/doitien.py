from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import requests
import datetime

converter = Tk()
converter.title("Currency Converter")
converter.geometry("600x250")

label1 = Label(converter, text = "Amount").grid(column = 0, row = 0)
label2 = Label(converter, text = "USD Currency Converter Using Python").grid(column = 1, row = 0, columnspan = 2)

value1 = DoubleVar()
value_box1 = Entry(converter, width = 25, textvariable = value1).grid(column = 0, row = 1, columnspan = 2, padx = 10, pady = 5)

value2 = DoubleVar()
value_box2 = Entry(converter, width = 25, textvariable = value2).grid(column = 0, row = 2, columnspan = 2, padx = 10, pady = 5)

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

currency_list = []
with open("API/bai 2/cl-currencies-table.txt","r") as read_file:
    content = read_file.readlines()
    for line in content:
        cleaned = line.strip()
        if "td" in cleaned and len(cleaned) == 12:
            cleaned = cleaned.strip("</td>")
            currency_list.append(cleaned)

c1["values"] = tuple(currency_list)
c2["values"] = tuple(currency_list)        


screen = Text(converter, width = 40, height = 5)
screen.grid(column = 1, row = 3, columnspan = 2, rowspan = 2, padx = 5)

def convert():
    currency_data = requests.get("http://api.currencylayer.com/live?access_key=4273d2c37f738367f08780b934ce7dda&format=1").json()
    currency1 = a.get()
    currency2 = b.get()
    currency_pair = currency1 + currency2
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
    price = round(price, 5)
    try:
        m = value1.get()
        n = value2.get()
        if n != 0:
            amount = round(1/(n*price), 5)
            value1.set(amount)
        amount = round(m*price, 5)
        value2.set(amount)
        screen.insert(END, "{} {} equals {} {}".format(value1.get(), currency1, value2.get(), currency2))
        screen.insert(END,"\nLast Time Update --- {}".format(datetime.datetime.fromtimestamp(currency_data["timestamp"])))
    except:
        screen.insert(END, "ERROR")


search = Button(converter, text = "Search", command = convert).grid(column = 0, row = 3)
clear = Button(converter, text = "Clear", command = lambda: screen.delete("1.0", END)).grid(column = 0, row = 4)

converter.mainloop()