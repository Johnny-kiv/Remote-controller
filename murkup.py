from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
btnP = KeyboardButton('+')
btnM = KeyboardButton("-")
btnPause = KeyboardButton("Пауза")
btnChoice = KeyboardButton("Выбрать фильм")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnM,btnP,btnPause,btnChoice)

btn1 = KeyboardButton('1')
btn2 = KeyboardButton('2')
btn3 = KeyboardButton('3')
btn4 = KeyboardButton('4')
btnExit = KeyboardButton('Домой')
choiceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1,btn2,btn3,btn4,btnExit)