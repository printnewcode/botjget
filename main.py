
import telebot

from telebot import types
bot = telebot.TeleBot('6406949709:AAHcb2HfRQase4k-oErBWcbMzA5VlNd-hCQ')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, это я Огр-Маг-Бот", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def textt(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if message.text == '👋 Поздороваться':
        video = open('C:/Users/acer 4/Downloads/videotg.mp4', 'rb')
        bot.send_video(message.chat.id, video, timeout=10)

bot.polling(none_stop=True, interval=0)
