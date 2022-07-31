import telebot
from telebot import types
import random
import markups as nav

token='5516460285:AAGL8WbF6WWqvm178wT_y71XVmldcW23bFM'

bot=telebot.TeleBot(token)
game = ['Ivan_Ivanonov', 'Ivan_Gabriel', 'Joseph_Krupi', 'Kany_West', 'Ben_Hllory', 'Vasya_Bomj', 'Georg_Washington', 'Kama_Pulya', 'Game_Over', 'Pizdec_SAMP']
cus = ['Для КСГО нету, пшел нахуй']


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!\nВыбери то что тебе надо снизу⬇️', reply_markup = nav.markup)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == '⌛Рандомайзер':
        bot.send_message(message.chat.id, 'До скольки?', reply_markup = nav.markup4)
    if message.text == '🧰Генератор ников':
        bot.send_message(message.chat.id, 'Какой тебе?', reply_markup = nav.markup2)
    if message.text == '🔙Назад':
        bot.send_message(message.chat.id, 'Привет!Выбери то что тебе надо снизу⬇️', reply_markup = nav.markup)
    if message.text == '🏦Ники SAMP':
        bot.send_message(message.chat.id, 'Твой ник:'+str(random.choice(game)))
    if message.text == '🔫Ники CS:GO':
        bot.send_message(message.chat.id, 'Для КСГО нету, я ленивый и не сделал')
    if message.text == '💾Другое':
        bot.send_message(message.chat.id, 'Хмммм, а что тут?', reply_markup = nav.markup3)
    if message.text == 'ℹ️ Информация':
        bot.send_message(message.chat.id, 'Бот создан человеком который знает ТелеБот 1 день. Создатель-@Licifersss')
    if message.text == 'До 100':
        bot.send_message(message.chat.id, 'Ваше число:'+ str(random.randint(0, 100)))
    if message.text == 'До 500':
        bot.send_message(message.chat.id, 'Ваше число:'+ str(random.randint(0, 500)))
    if message.text == 'До 1000':
    	bot.send_message(message.chat.id, 'Ваше число:'+ str(random.randint(0, 1000)))
    if message.text == '📦Секретная коробка':
        bot.send_message(message.chat.id, ' В коробке....Барабанная дробь.... НИ-ЧЕ-ГО')
    if message.text == '👩‍💻Связь с создателем':
        bot.send_message(message.chat.id, 'Создатель-[Легенда](https://t.me/GhostRiver/)', parse_mode='Markdown')

bot.polling(none_stop = True)
