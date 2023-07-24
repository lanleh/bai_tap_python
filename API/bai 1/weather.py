from tkinter import *
from datetime import *
from PIL import ImageTk, Image
import requests

weather = Tk()
weather.title("Weather Application")
weather.geometry("500x400")

top_frame = Frame(weather, bg = "midnight blue")
top_frame.place(relheight = 0.1, relwidth = 1)

mid_frame1 = Frame(weather)
mid_frame1.place(relheight = 0.3, relwidth = 1, rely = 0.1)

mid_frame2 = Frame(weather, bg = "midnight blue")
mid_frame2.place(relheight = 0.05, relwidth = 1, rely = 0.4)

bottom_frame = Frame(weather)
bottom_frame.place(relheight = 0.55, relwidth = 1, rely = 0.45)


placeholder1 = Label(top_frame, text = "NA-/", fg = "white", bg = "midnight blue", font = ("Tahoma", 10, "bold"))
placeholder1.place(relx = 0, rely = 0.2)

center1 = Label(top_frame, text = "Weather Report", fg = "white", bg = "midnight blue", font = ("Tahoma", 10, "bold"))
center1.place (relx = 0.375, rely = 0.2)

calendar = Label(top_frame, text = date.today(), fg = "white", bg = "midnight blue", font = ("Tahoma", 10, "bold"))
calendar.place(relx = 0.8, rely = 0.2)


image1 = Image.open("API/bai 1/sun.jpg")
sun = ImageTk.PhotoImage(image1)

icon1 = Label(mid_frame1, image = sun)
icon1.grid(column = 0, row = 0, rowspan = 3, ipadx = 10)

box_title = Label(mid_frame1, text = "City or Country Name", fg = "midnight blue", font = ("Tahoma", 10, "bold")).grid(column = 1, row = 0)
city = StringVar()
city_name = Entry(mid_frame1, width = 30,  textvariable = city)
city_name.grid(column = 1, row = 1)

center2 = Label(mid_frame2, text = "Weather Report", bg = "midnight blue", fg = "white", font = ("Tahoma", 10, "bold")).pack(side = TOP)

image2 = Image.open("API/bai 1/clouds.jpg")
clouds = ImageTk.PhotoImage(image2)
icon2 = Label(bottom_frame, image = clouds)
icon2.grid(column = 0, row = 0, ipadx = 20, ipady = 20)
placeholder2 = Label(bottom_frame, text = "NA/-", fg = "midnight blue", font = ("Tahoma", 10, "bold"))
placeholder2.grid(column = 0, row = 1)


image3 = Image.open("API/bai 1/temp.jpg")
temp = ImageTk.PhotoImage(image3)
icon3 = Label(bottom_frame, image = temp)
icon3.grid(column = 1, row = 0, ipadx = 20, ipady = 20)
placeholder3 = Label(bottom_frame, text = "NA/-", fg = "midnight blue", font = ("Tahoma", 10, "bold"))
placeholder3.grid(column = 1, row = 1)


image4 = Image.open("API/bai 1/rain.jpg")
rain = ImageTk.PhotoImage(image4)
icon4 = Label(bottom_frame, image = rain)
icon4.grid(column = 2, row = 0, ipadx = 20, ipady = 20)
placeholder4 = Label(bottom_frame, text = "NA/-", fg = "midnight blue", font = ("Tahoma", 10, "bold"))
placeholder4.grid(column = 2, row = 1)

image5=Image.open("API/bai 1/wind.jpg")
wind = ImageTk.PhotoImage(image5)
icon5 = Label(bottom_frame, image = wind)
icon5.grid(column = 3, row = 0, ipadx = 20, ipady = 20)
placeholder5 = Label(bottom_frame, text = "NA/-", fg = "midnight blue", font = ("Tahoma", 10, "bold"))
placeholder5.grid(column = 3, row = 1)


def data_retrieval():
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    api_key = "fe53bfd100e8ca1c2ca47f202a2e9b9c"
    complete_link = url + city.get()+api_key
    print(complete_link)
    #weather_data = requests.get(url+city.get()+api_key).json()
    #print(weather_data)

search = Button(mid_frame1, text = "Search", command = data_retrieval).grid(column = 2, row = 1)


weather.mainloop()

