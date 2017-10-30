import vk
import getpass

APP_ID = 6238089


def get_user_login():
    user_login = input('Введите свой логин:\n')
    return user_login


def get_user_password():
    user_password = getpass.getpass(prompt='Введите свой пароль:\n')
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
    print('Сейчас в онлайне след. пользователи:\n')
    users_info = vk_session.users.get(user_ids=friends_online_ids)
    for user in users_info:
        print('{} {}'.format(user['first_name'], user['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    vk_session = create_vk_session(login, password)
    friends_online_ids = get_online_friends_ids(vk_session)
    output_friends_to_console(friends_online_ids, vk_session)
