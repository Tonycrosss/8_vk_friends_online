import vk
import time


APP_ID = 6238089  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    user_login = input('Введите свой логин:\n')
    return user_login


def get_user_password():
    user_password = input('Введите свой пароль:\n')
    return user_password


def create_vk_session(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    return api


def get_online_friends_ids(vk_session):
    friends_online_ids = vk_session.friends.getOnline()
    return friends_online_ids


def output_friends_to_console(friends_online_ids, vk_session):
    fio_list = []
    print('Сейчас в онлайне след. пользователи:\n')
    for user_id in friends_online_ids:
        user_info = vk_session.users.get(user_id=user_id)[0]
        fio_list.append(user_info['first_name'] + ' ' + user_info['last_name'])
        time_count = 1
        time.sleep(time_count)

    for fio in fio_list:
        print(fio)


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    vk_session = create_vk_session(login, password)
    friends_online_ids = get_online_friends_ids(vk_session)
    output_friends_to_console(friends_online_ids, vk_session)
