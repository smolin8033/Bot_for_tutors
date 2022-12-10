# flake8: noqa

from aiogram import Bot, Dispatcher

from config.conf import settings

# DONE data transfer object (создать Dataclass User поля username telegram_id) dataclasses python
# DONE обработка ответа вы зарегистрировались, вы не зарегистрировались
# DONE залогировать такой-то пользователь залогировался или нет
# DONE url вынести в настройки
# DONE api папка там файл с отправкой api

# TODO при регистрации имя фамилия (либо учитель, либо ученик)
# TODO с телеграма header каждый раз отправлять, заголовок "user_id" там telegram_id/ если нет авторизуйся, если есть, то распознать пользователя
# TODO во вьюсете обработка хедеров, есть искать пользователя по хедеру и определять, кто он
# TODO учитель может добавить учеников, создать уникальная ссылка на себя, он пересылает ученику, а ученик может отправить боту эту ссылку и присоединяет ученика к учителю в пермишионах смотреть статус
# TODO сохранить пользователя в кэше и сделать периодическую задачу смотреть скэшировано или нет
# TODO если можно tests если найти как делать

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)
