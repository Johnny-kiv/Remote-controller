import os
from aiogram import Bot,Dispatcher,executor,types
from config import bot_token,admin
import murkup as nav
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
os.system("amixer -c 0 set Master 80%")
v = 80
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,"Привет!".format(message.from_user),reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    global v
    if message.text == "+":
        v += 2
        os.system(f"amixer -c 0 set Master {v}%")
        await bot.send_message(message.from_user.id,v,reply_markup=nav.mainMenu)
    if message.text == "-":
        v -= 2
        os.system(f"amixer -c 0 set Master {v}%")
        await bot.send_message(message.from_user.id,v,reply_markup=nav.mainMenu)
    if message.text == "Выбрать фильм":
        await bot.send_message(message.from_user.id,"1.Стартрек Первый",reply_markup=nav.choiceMenu)
        await bot.send_message(message.from_user.id,"2.Стартрек Второй", reply_markup=nav.choiceMenu)
        await bot.send_message(message.from_user.id,"3.Стартрек Третий", reply_markup=nav.choiceMenu)
        await bot.send_message(message.from_user.id,"4.Belliver", reply_markup=nav.choiceMenu)
        await bot.send_message(message.from_user.id,"5.Гарфилд Первый", reply_markup=nav.choiceMenu)
        await bot.send_message(message.from_user.id,"6.Гарфилд Второй", reply_markup=nav.choiceMenu)
        await bot.send_message(message.from_user.id,"7.Тор", reply_markup=nav.choiceMenu)
        await bot.send_message(message.from_user.id,"8.Тор Царство Тьмы", reply_markup=nav.choiceMenu)
        await bot.send_message(message.from_user.id,"9.Тор Рагнарёк", reply_markup=nav.choiceMenu)
    if message.text=="1":
        os.system("xdg-open /home/user/Видео/Zvezdnij.put.2009.XviD.DVDRip.ELEKTRI4KA.avi")
    if message.text=="2":
        os.system("xdg-open /home/user/Видео/Startrek.Vozmezdie.2013.RUS.BDRip.XviD.AC3.-HQ-ViDEO.avi")
    if message.text=="3":
        os.system("xdg-open /home/user/Видео/StarTrekBeyond.avi")
    if message.text=="4":
        os.system("xdg-open /home/user/Видео/Beliver.mp4")
    if message.text == "5":
        os.system("xdg-open /home/user/Видео/Garfild.2004.XviD.DVDRip.Kinozal.TV.avi")
    if message.text == "6":
        os.system("xdg-open /home/user/Видео/Гарфилд 2. История двух кошечек.mkv")
    if message.text == "7":
        os.system("xdg-open /home/user/Видео//home/user/2011-Thor.avi")
    if message.text == "8":
        os.system("xdg-open /home/user/Видео/Beliver.mp4")
    if message.text == "9":
        os.system("xdg-open /home/user/Видео/Beliver.mp4")
    if message.text=="Домой":
        await bot.send_message(message.from_user.id,"Главная",reply_markup=nav.mainMenu)
    if message.text == "Пауза":
        os.system("qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates= True)
#название::зп:фирма::место::ссылка