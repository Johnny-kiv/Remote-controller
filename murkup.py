import os
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
# Основное меню
# Кнопки изменения громкости
btnP = KeyboardButton('➕')
btnM = KeyboardButton("➖")
btnV = KeyboardButton('⏩')
btnN = KeyboardButton("⏪")
btnF = KeyboardButton("↕️")
# Пауза
btnPause = KeyboardButton("⏯")
# Кнопка перехода на другое меню
btnChoice = KeyboardButton("Выбрать фильм")
# Отоброжение кнопок основного меню
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnM,btnP,btnF,btnN,btnPause,btnV,btnChoice)
# Меню выбора фильма
def choice():
    lis = os.listdir(path='/home/user/Видео')
    choiceMenu = InlineKeyboardMarkup(row_width=1)
    for i in lis:
        choiceMenu.insert(InlineKeyboardButton(text=f"{i}",callback_data=f"/{i}"))
    return choiceMenu



