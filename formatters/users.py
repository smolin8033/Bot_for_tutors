def get_first_and_last_name(users: list) -> list:
    """
    Make a list representation of users' first name and last name
    """
    users_data = [[user.get("first_name"), user.get("last_name")] for user in users]
    return users_data


def make_string_representation(names: list) -> str:
    """
    Make a good-looking Telegram UI str representation of users
    """
    users_list_data: list = [" ".join([str(x) for x in lst]) for lst in names]

    users_string_data: str = "\n".join(users_list_data)
    return users_string_data
