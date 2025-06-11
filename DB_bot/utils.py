# utils.py
from telebot import types

def gen_inline_markup(rows):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    for row in rows:
        markup.add(types.InlineKeyboardButton(row, callback_data=row))
    return markup

def gen_markup(rows):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 1
    for row in rows:
        markup.add(types.KeyboardButton(row))
    markup.add(types.KeyboardButton("Отмена 🚫"))
    return markup
