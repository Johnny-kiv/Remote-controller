#!/usr/bin/python3
#Подключаем нужные библиотеки
import os
from aiogram import Bot, Dispatcher, executor, types
from config import bot_token, admin
import murkup as nav

#создаем объекты и первоначальные переменные
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
os.system("amixer -c 0 set Master 80%")
v = 80

#Приветствие по команде старт
@dp.message_handler(commands=['start'])
async def command_start(mes: types.Message):
    await bot.send_message(mes.from_user.id, "Привет!", reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(mes: types.Message):
    global v
    #Регулируем громкость
    if mes.text == "➕":
        await bot.delete_message(mes.from_user.id, mes.message_id)
        v += 2
        os.system(f"amixer -c 0 set Master {v}%")
        await bot.send_message(admin, f"Громкость: {v}%", reply_markup=nav.mainMenu)
    if mes.text == "➖":
        await bot.delete_message(mes.from_user.id, mes.message_id)
        v -= 2
        os.system(f"amixer -c 0 set Master {v}%")
        await bot.send_message(admin, f"Громкость: {v}%", reply_markup=nav.mainMenu)
    #Промотка вперед
    if mes.text == "⏩":
        await bot.delete_message(mes.from_user.id, mes.message_id)
        os.system( "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Seek int64:10000000")
    if mes.text == "⏪":
        await bot.delete_message(mes.from_user.id, mes.message_id)
        os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Seek int30:10000000")
    if mes.text == "↕️":
        await bot.delete_message(mes.from_user.id, mes.message_id)
        os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.fullscreen")
    if mes.text == "Выбрать фильм":
        await bot.delete_message(mes.from_user.id, mes.message_id)
        await bot.send_message(admin, "Выберете фильм", reply_markup=nav.choice())
    if mes.text == "⏯":
        os.system("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")
        await bot.delete_message(mes.from_user.id, mes.message_id)
        await bot.send_message(admin, "Фильм либо остановлен, либо включен.", reply_markup=nav.mainMenu)


@dp.callback_query_handler(text_contains="/")
async def open_m(call: types.CallbackQuery):
    os.system(f"xdg-open /home/user/Видео{call.data}")
    await bot.send_message(admin, "Фильм включен. Приятного просмотра! 🙂", reply_markup=nav.mainMenu)
    await bot.delete_message(call.from_user.id,call.message.message_id)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
