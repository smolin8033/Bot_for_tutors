from aiogram import types

from keyboards.buttons import student, teacher

inline_keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(teacher, student)
