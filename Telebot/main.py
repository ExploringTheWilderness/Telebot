import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

TOKEN = '6866465068:AAFRAzEPQO9lslnlK5CjtPmvbrGzWErF3Mw'
bot = telebot.TeleBot(TOKEN)

motivational_images = [
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwkPL32mhfJ0lAtfLqjUNG9EvRFlmGZmFloROaPvGGfg&s',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTE7b3Hj2Z939UO2qoO0kcU1KcOr5-598sojZhka6RyCw&s',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3NAiye-JeCh9Gn9n2sp0aAudXrFheZOKE7QPGQn13ZQ&s',
]

def generate_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Получить мотивацию", callback_data="get_motivation"))
    return markup

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку ниже, чтобы получить мотивацию.", reply_markup=generate_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "get_motivation":
        img_url = random.choice(motivational_images)
        bot.send_photo(call.message.chat.id, img_url)

    bot.send_message(call.message.chat.id, "Хочешь еще мотивации?", reply_markup=generate_markup())

bot.polling(none_stop=True)