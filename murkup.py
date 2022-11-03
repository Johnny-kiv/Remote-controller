from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# Основное меню
# Кнопки изменения громкости
btnP = KeyboardButton('+')
btnM = KeyboardButton("-")
# Пауза
btnPause = KeyboardButton("Пауза")
# Кнопка перехода на другое меню
btnChoice = KeyboardButton("Выбрать фильм")
# Отоброжение кнопок основного меню
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnM,btnP,btnPause,btnChoice)
# Меню выбора фильма
# Можете добавить еще фильмы по количеству кнопок
btn1 = KeyboardButton('1')
btn2 = KeyboardButton('2')
btn3 = KeyboardButton('3')
btn4 = KeyboardButton('4')
btn5 = KeyboardButton('5')
btn6 = KeyboardButton('6')
btn7 = KeyboardButton('7')
btn8 = KeyboardButton('8')
btn9 = KeyboardButton('9')
btnExit = KeyboardButton('Домой')
choiceMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1,btn2,btn3,btn4,btn8,btn9,btnExit)