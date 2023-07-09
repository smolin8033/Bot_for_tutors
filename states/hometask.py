from aiogram.dispatcher.filters.state import State, StatesGroup


class HometaskStatesGroup(StatesGroup):
    name = State()
    start_datetime = State()
    end_datetime = State()
    coursebook = State()
    exercises = State()
    url = State()
    more_info = State()
