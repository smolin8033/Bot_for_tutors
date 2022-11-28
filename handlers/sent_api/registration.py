import requests


def send_registration_data(user_id, username):
    url = 'http://89.108.76.250/api/telegram_users/'
    data = {
        "username": username,
        "telegram_id": user_id
    }
    result = requests.post(url=url, data=data)
    return result
