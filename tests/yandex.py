import requests

TOKEN = input('Write your token here: ')
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(path):
    res = requests.put(f'{URL}?path={path}', headers=headers)
    return res.status_code


def delete_folder(path):
    res = requests.delete(f'{URL}?path={path}', headers=headers)
    return res.status_code


def check_file(path):
    res = requests.get(f'{URL}?path={path}', headers=headers)
    return res.status_code


def test_creating_folder_with_deleting(path='test'):
    result = create_folder(path)
    # 201 - успешно добавлен
    # 409 - уже существует
    if result == 409 and delete_folder(path) == 204:
        result = create_folder(path)
    assert result == 201, 'Тест №1 не пройден'


def test_creating_already_existed_file(path='test'):
    if check_file(path) == 200:
        create_folder(path)
    result = create_folder(path)
    # 201 - успешно добавлен
    # 409 - уже существует
    assert result != 201, 'Тест №2 не пройден'


def test_check_file_existed(path='test'):
    result = check_file(path)
    if result != 200:
        create_folder(path)
        result = check_file(path)
    assert result == 200, 'Тест №3 не пройден'


def test_check_file_non_existed(path='test'):
    result = check_file(path)
    if result == 200:
        tmp = delete_folder(path)
        result = check_file(path)
    assert result != 200, 'Тест №4 не пройден'


def check_token():
    res = check_file('test')
    return res != 401  # not authorized


if check_token():
    test_creating_folder_with_deleting()
    test_creating_already_existed_file()
    test_check_file_existed()
    test_check_file_non_existed()
else:
    print('Incorrect token')
