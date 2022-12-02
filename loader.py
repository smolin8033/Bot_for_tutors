from aiogram import Bot, Dispatcher

from config.conf import settings

# TODO poetry вместо requirements
# TODO async запросы только можно httpx/aiohttp
# TODO make timeout python
# TODO обработка ответа вы зарегистрировались, вы не зарегистрировались
# TODO залогировать такой-то пользователь залогировался или нет
# TODO url вынести в настройки
# TODO data transfer object (создать Dataclass User поля username telegram_id) dataclasses python
# TODO api папка там файл с отправкой api
# TODO если можно tests если найти как делать
# TODO при регистрации имя фамилия (либо учитель, либо ученик)
# TODO учитель может добавить учеников, создать уникальная ссылка на себя, он пересылает ученику, а ученик может отправить боту эту ссылку и присоединяет ученика к учителю в пермишионах смотреть статус

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(bot)