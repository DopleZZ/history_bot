from telebot import types

keyboard1 = types.InlineKeyboardMarkup()
key_find = types.InlineKeyboardButton(text='Искать', callback_data='to_find')
keyboard1.add(key_find)