from tkinter import *
from tkinter.ttk import *
import googletrans
from googletrans import Translator
from PIL import Image, ImageTk

ggdich = Tk()
ggdich.title("Language Translator")
ggdich.geometry("600x350")

tudien = Image.open("API/bai 3/tudien.jpg")
processed_image = ImageTk.PhotoImage(tudien)
logo = Label(ggdich, image = processed_image).grid(column = 2, row = 0, pady = 10)

lang_dict = googletrans.LANGCODES
languages = list(lang_dict.keys())
languages = [lang.capitalize() for lang in languages]

source_lang = StringVar(ggdich, "Auto Detect")
option1 = Combobox(ggdich, width = 25, textvariable = source_lang)
option1["values"] = ["Auto Detect"] + languages
option1.grid(column = 1, row = 1, padx = 10)

dest_lang = StringVar()
option2 = Combobox(ggdich, width = 25, textvariable = dest_lang, values = languages)
option2.grid(column = 3, row = 1, padx = 10)

source_screen = Text(ggdich, height = 10, width = 30)
source_screen.grid(column = 1, row = 2, padx = 5, pady = 5)

dest_screen = Text(ggdich, height = 10, width = 30)
dest_screen.grid(column = 3, row = 2, padx = 5, pady = 5)

def trans():
    translator = Translator()
    input = source_screen.get("1.0", END)
    if source_lang.get() == "Auto Detect":
        code1 = "auto"
    else:
        a = source_lang.get().lower()
        code1 = lang_dict[a]
    b = dest_lang.get().lower()
    code2 = lang_dict[b]
    res = translator.translate(input, src = code1, dest = code2)
    output = res.text
    dest_screen.insert(END, output)

def erase():
    source_lang.set("Auto Detect")
    dest_lang.set("")
    source_screen.delete("1.0", END)
    dest_screen.delete("1.0", END)

action = Button(ggdich, text = "Translate", command = trans).grid(column = 1, row = 3, pady = 5)
eraser = Button(ggdich, text = "Clear", command = erase).grid(column = 3, row = 3, pady = 5)

ggdich.mainloop()