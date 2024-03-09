import json
from datetime import date


def get_list():
    """Функция считывает json файл преобразует его список"""
    with open('OPERATIONS_FILE', 'r', encoding='utf-8') as json_data_cart:
        data_cart = json.load(json_data_cart)
        return data_cart


def get_last_five_operations(data_cart):
    """Функция проверяет есть date в операциях и сортирует список операций по дате и возвращает 5 последних"""
    suitable_file = True
    n = 0
    for operations in data_cart:
        if 'date' not in operations:
            n += 1
            suitable_file = False
            break
    if suitable_file == True:
        data_cart.sort(key=lambda dictionary: dictionary['date'])
        return data_cart[-5:]
    else:
        return f"Отсутствует дата в операции номер - {n}"


def formation_date(last_five_operations_cart):
    """Функция форматирует дату под требования задния"""

    for operations in last_five_operations_cart:
        if len(operations["date"]) >= 10:
            operations["date"] = operations["date"][:10]
            date_operations = date.fromisoformat(operations['date'])
            operations['date'] = date_operations.strftime("%d.%m.%Y")
            return last_five_operations_cart
        else:
            return f'Ошибка даты: слинком короткая строка'


def add_from_in_operations(last_five_operations_cart):
    """Функция проверян наличее срета отправителя и обавляет ключ from и значение 'Отсутствует' если такого ключа нет"""
    for operations in last_five_operations_cart:
        if len(operations) == 6:
            operations["from"] = "Отсутствует"
    return last_five_operations_cart


def disguise_sender_account(last_five_operations_cart):
    """Функция маскерует номер счета отправителя отображая первые 6 цифр и последние 4 цифры"""
    for operations in last_five_operations_cart:
        if operations["from"] != "Отсутствует":
            operations["from"] = operations["from"][:-10] + "*" * 6 + operations["from"][-4:]
    return last_five_operations_cart


def disguise_recipients_account(last_five_operations_cart):
    """Функция маскерует номер счета получателя отображая только последние 4 цифры"""
    for operations in last_five_operations_cart:
        list_operations_to = operations["to"].split()
        cart = " ".join(list_operations_to[:-1])
        check = " ".join(list_operations_to[-1:])
        operations["to"] = cart + " **" + check[-4:]
    return last_five_operations_cart


