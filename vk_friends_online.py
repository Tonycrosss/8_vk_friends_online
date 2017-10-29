import vk


APP_ID = 6238089  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    user_login = input('Введите свой логин:\n')
    return user_login


def get_user_password():
    user_password = input('Введите свой пароль:\n')
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    # например, api.friends.get()
    print(api.friends.get())


def output_friends_to_console(friends_online):
    pass


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
