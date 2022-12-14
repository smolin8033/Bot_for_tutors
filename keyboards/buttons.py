from aiogram import types

from keyboards.callback_data import callback_data_base_menu

teacher = types.InlineKeyboardButton(text="Teacher", callback_data=callback_data_base_menu.new(id=1, action="teacher"))
student = types.InlineKeyboardButton(text="Student", callback_data=callback_data_base_menu.new(id=2, action="student"))
