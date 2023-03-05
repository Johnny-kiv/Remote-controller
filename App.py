#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
import os

def show_message():
    config = open("config.py","w")
    tokenT = token.get()
    adminT = admin.get()
    config.write(f"bot_token = '{tokenT}'"+"\n")
    config.write(f"admin = '{adminT}'")
    config.close()
    os.system("./main.py")
root = Tk()
root.title("Remote controller")
root.geometry("250x150")
tokenL = Label(text="Введите токен вашего бота:")
tokenL.pack()
token = ttk.Entry()
token.pack(anchor=NW, padx=6, pady=6)
adminL = Label(text="Введите ваш id:")
adminL.pack()
admin = ttk.Entry()
admin.pack(anchor=NW, padx=6, pady=7)

btn = ttk.Button(text="Запуск бота", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)
root.mainloop()