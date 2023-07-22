from tkinter import *
from datetime import *

weather = Tk()
weather.title("Weather Application")
weather.geometry("500x400")

top_frame = Frame(weather, bg = "midnight blue")
top_frame.place(height = 40, relwidth = 1)


city_name = Label(top_frame, text = "NA-/", fg = "white", bg = "midnight blue", font = ("Tahoma", 10, "bold"))
city_name.place(relx = 0, rely = 0.2)

center1 = Label(top_frame, text = "Weather Report", fg = "white", bg = "midnight blue", font = ("Tahoma", 10, "bold"))
center1.place (relx = 0.375, rely = 0.2)

calendar = Label(top_frame, text = date.today(), fg = "white", bg = "midnight blue", font = ("Tahoma", 10, "bold"))
calendar.place(relx = 0.8, rely = 0.2)

mid_frame = Frame(weather)
mid_frame.place(relwidth = 1)




weather.mainloop()

