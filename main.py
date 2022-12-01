#!/usr/bin/python3
import os
from aiogram import Bot, Dispatcher, executor, types
from config import bot_token, admin
import murkup as nav

bot = Bot(token=bot_token)
dp = Dispatcher(bot)
os.system("amixer -c 0 set Master 80%")
v = 80

@dp.message_handler(commands=['start'])
async def command_start():
    await bot.send_message(admin, "Привет!", reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    global v
    if message.text == "➕":
        v += 2
        os.system(f"amixer -c 0 set Master {v}%")
        await bot.send_message(message.from_user.id, f"Громкость: {v}%", reply_markup=nav.mainMenu)
    if message.text == "➖":
        v -= 2
        os.system(f"amixer -c 0 set Master {v}%")
        await bot.send_message(message.from_user.id, f"Громкость: {v}%", reply_markup=nav.mainMenu)
    if message.text == "⏩":
        os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Seek int64:10000000")
    if message.text == "⏪":
        os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Seek int30:10000000")
    if message.text == "↕️":
        os.system("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.fullscreen")
    if message.text == "Выбрать фильм":
        await bot.send_message(message.from_user.id, "Выберете фильм", reply_markup=nav.choiceMenu)
    if message.text == "⏯":
        os.system("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")
        await bot.send_message(message.from_user.id, "Фильм либо остановлен, либо включен.", reply_markup=nav.mainMenu)

#Включение фильма
@dp.callback_query_handler(text_contains="/")
async def open_m(call: types.CallbackQuery):
    os.system(f"xdg-open <Ваша папка>{call.data}")
    await bot.send_message(call.from_user.id, "Фильм включен. Приятного просмотра! 🙂", reply_markup=nav.mainMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)