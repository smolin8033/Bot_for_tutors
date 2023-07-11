from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram_calendar import SimpleCalendar, simple_cal_callback

from loader import bot, dp
from states.hometask import HometaskStatesGroup


@dp.message_handler(commands=["create_task"])
async def create_task(message: types.Message) -> None:
    await message.answer("Let's create a new hometask. To begin with, send me a name of hometask.")
    await HometaskStatesGroup.name.set()


@dp.message_handler(state=HometaskStatesGroup.name)
async def load_name(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["name"] = message.text

    await message.answer("Now, when can your student start doing this hometask?")
    await message.answer("Please, select a date: ", reply_markup=await SimpleCalendar().start_calendar())

    await HometaskStatesGroup.next()


@dp.callback_query_handler(simple_cal_callback.filter(), state=HometaskStatesGroup.start_datetime)
async def process_start_datetime(callback_query: CallbackQuery, callback_data: dict, state: FSMContext) -> None:
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)

    if selected:
        async with state.proxy() as data:
            data["start_datetime"] = date

        await callback_query.message.answer("Your choice is accepted.")

        await HometaskStatesGroup.next()

        await load_end_datetime(state)


async def load_end_datetime(state: FSMContext) -> None:
    # async with state.proxy() as data:
    #     data["end_datetime"] = 'random'

    await bot.send_message(state.chat, "Now, when is the deadline for this homework?")
    await bot.send_message(state.chat, "Please, select a date: ", reply_markup=await SimpleCalendar().start_calendar())


@dp.callback_query_handler(simple_cal_callback.filter(), state=HometaskStatesGroup.end_datetime)
async def process_end_datetime(callback_query: CallbackQuery, callback_data: dict, state: FSMContext) -> None:
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)

    if selected:
        async with state.proxy() as data:
            data["end_datetime"] = date

        await callback_query.message.answer("Your choice is accepted.")

        await HometaskStatesGroup.next()

        await load_coursebook(state)


@dp.message_handler(state=HometaskStatesGroup.coursebook)
async def load_coursebook(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["coursebook"] = message.text

    async with state.proxy() as data:
        await message.answer(data)

    await HometaskStatesGroup.next()
