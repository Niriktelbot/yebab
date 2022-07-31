from telebot import types


markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
but1=types.KeyboardButton('⌛Рандомайзер')
but2=types.KeyboardButton('🧰Генератор ников')
but3=types.KeyboardButton('💾Другое')
but4=types.KeyboardButton('ℹ️ Информация')

markup.add(but1, but2, but3, but4)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
nik = types.KeyboardButton('🏦Ники SAMP')
csgo = types.KeyboardButton('🔫Ники CS:GO')
back = types.KeyboardButton('🔙Назад')
markup2.add(nik, csgo, back)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard = True)
koroba = types.KeyboardButton('📦Секретная коробка')
svyaz = types.KeyboardButton('👩‍💻Связь с создателем')
back2 = types.KeyboardButton('🔙Назад')
markup3.add(koroba, svyaz, back2)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard = True)
sto = types.KeyboardButton('До 100')
pyat = types.KeyboardButton('До 500')
tus = types.KeyboardButton(' До 1000')
back3 = types.KeyboardButton('🔙Назад')
markup4.add(sto, pyat, tus, back3)

