# flake8: noqa

from aiogram import Bot, Dispatcher

from config.conf import settings

# front:
# TODO учитель может добавить учеников, создать уникальная ссылка на себя, он пересылает ученику, а ученик может отправить боту эту ссылку и присоединяет ученика к учителю в пермишионах смотреть статус (many to many  на self)
# TODO сохранить пользователя в кэше и сделать периодическую задачу смотреть скэшировано или нет
# TODO если можно tests если найти как делать

# back:
#  TODO dumpdata
#  TODO CRUD User (это в принципе не нужно, мб что-то из)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)
