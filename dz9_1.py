import json

users = [{'email': 'some@mail.ru', 'password': '123pass'}]
try:
    with open('data_file_with_users.json', 'r') as data:
        users = json.load(data)
except FileNotFoundError:
    with open('data_file_with_users.json', 'w') as data_file_with_users:
        json.dump(users, data_file_with_users)
    with open('data_file_with_users.json', 'r') as data:
        users = json.load(data)


def get_email():
    x = input('Введите email\n')
    return x


def get_password():
    y = input('Введите пароль\n')
    return y


def check_data(a, b):
    with open('data_file_with_users.json', 'r') as data:
        new_data = json.load(data)
    for i in new_data:
        if i['email'] == a and i['password'] == b:
            print('You enter successfully')
            return a
    else:
        return (print("Error"))


def registration():
    new_email = get_email()
    with open('data_file_with_users.json', 'r') as data_new:
        users_new = json.load(data_new)
        email_is_exist = False
        for i in users_new:
            if new_email == i['email']:
                email_is_exist = True
        if email_is_exist:
            print('Enter new email')
            registration()
        else:
            new_password = get_password()
            pass_check = input('Enter password one more time\n')
            if pass_check == new_password:
                users_new.append({'email': new_email, 'password': new_password})
                with open('data_file_with_users.json', 'w') as data_file_with_users_new:
                    json.dump(users_new, data_file_with_users_new)
                print('Registration finished')
                quit()
            else:
                print('Error')
                quit()

    return None


def function_for_users():
    a = input('If you want enter - press 1, '
                  'If you want registration - press 2\n')
    if a == '1' or a == '2':
        a = int(a)
    else:
        print('Enter only numbers 1 or 2')
    if a == 1:
        check_data(get_email(), get_password())
        quit()
    if a == 2:
        registration()

    return None


function_for_users()