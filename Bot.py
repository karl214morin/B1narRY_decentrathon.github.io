import telebot
from telebot import types
from telebot.types import WebAppInfo

bot = telebot.TeleBot('7438370613:AAFsjgOjctysXl_lZSRKLVc4rFn5kXv5pVY')

@bot.message_handler(commands=["start"])
def get_message(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = (types.InlineKeyboardButton("quiz", web_app = WebAppInfo('https://karl214morin.github.io/newsmth.github.io/') ))
    markup.row(btn1)
    bot.reply_to(message,"Hello! \n It telegram mini app project. \n there you can start studying:", reply_markup = markup)


bot.polling(none_stop = True)