import requests

def send_registration_data(user_id, username):
    url = 'http://localhost/api/telegram_users/'
    data = {
        "username": username,
        "telegram_id": user_id
    }
    result = requests.post(url=url, data=data)
    return result
