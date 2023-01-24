# flake8: noqa

from aiogram import Bot, Dispatcher

from config.conf import settings

# DONE data transfer object (создать Dataclass User поля username telegram_id) dataclasses python
# DONE обработка ответа вы зарегистрировались, вы не зарегистрировались
# DONE залогировать такой-то пользователь залогировался или нет
# DONE url вынести в настройки
# DONE api папка там файл с отправкой api
# DONE при регистрации имя фамилия (либо учитель, либо ученик) бот отправляет, бек принимает
# DONE таймаут ошибка + сервер не работает + 500 ошибка(в бекенде при обработке запроса выкинуть 500 ошибку) get_queryset timesleep 2 sec raise HTTPs ERROR или apiexception + остановка контейнеров (sentry посмотреть)
# DONE middleware получать запрос брать телеграм ид из хедера если нет требовать и распознать пользователя по наличию в в headers telegram_id, потом в request.users засовывать юзер

# typehints?
# TODO сообщение со списком учеников и учителей по /list_of в телеграме
# TODO учитель может добавить учеников, создать уникальная ссылка на себя, он пересылает ученику, а ученик может отправить боту эту ссылку и присоединяет ученика к учителю в пермишионах смотреть статус (many to many  на self)

# TODO сохранить пользователя в кэше и сделать периодическую задачу смотреть скэшировано или нет
# TODO если можно tests если найти как делать

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)
