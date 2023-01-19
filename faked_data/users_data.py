from random import choice

from faker import Faker

from entities import User

fake = Faker()

faked_user1 = User(
    first_name=fake.name().split(" ")[0],
    last_name=fake.name().split(" ")[1],
    username=fake.lexify(text="???????????"),
    telegram_id=fake.msisdn(),
    role=choice(["teacher", "student"]),
)
