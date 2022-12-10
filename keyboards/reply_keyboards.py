from aiogram import types

from keyboards.buttons import student, teacher

reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(teacher, student)
