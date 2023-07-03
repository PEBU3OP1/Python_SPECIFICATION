"""1. Напишите функцию для транспонирования матрицы"""
matrix = [[1, 2, 3, 4]]

def matrix_transponse(matrix: list)-> list:
    transp_matrix = []
    for x in range(len(matrix[0])):
        tmp = []
        for y in range(len(matrix)):
            tmp.append(matrix[y][x])
        transp_matrix.append(tmp)
    return transp_matrix

print(matrix_transponse(matrix))

"""
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного
аргумента. Если ключ не хешируем, используйте его строковое представление
"""

def only_key_params(**kwargs):
    voc_to_return = {}
    for key, val in kwargs.items():
        if isinstance(val, (list, dict, set, bytearray)):
            for v in val:
                voc_to_return[v] = str(key)
        else:
            voc_to_return[val] = key
    print(voc_to_return)
only_key_params(dfds = 2, gr = [44, 33], dfd = {1,3})

"""
Дополнить задачу из семинара 2. Сохраняйте все операции поступления и снятия
"""


import datetime
def add_bank(cash: int):
    global bank, count
    bank += cash
    count += 1
    print('Ваш баланс: ', bank)
    return cash


def take_bank(cash):
    global bank, count
    if cash < bank:
        if (cash / 100 * 1.5) < 30:
            bank -= 30
        elif 30 < (cash / 100 * 1.5) < 600:
            bank -= cash / 100 * 1.5
        elif (cash / 100 * 1.5) > 600:
            bank -= 600
    else:
        print('Недостаточно средств!')
    bank -= cash
    count += 1
    print('Ваш баланс: ', bank)
    return cash


def check_bank() -> int:
    while True:
        cash = int(input('Введите сумму кратную 50 '))
        if cash % 50 == 0:
            return cash


def bancomat():
    global bank, count
    bank = 5000
    operations_dict = {}
    count = 0
    while True:
        action = int(input('1 - снять\n2 - пополнить\n3 - выйти\n'))
        if bank >= 5_000_000:
            bank *= 0.9

        if action == 1:
            operations_dict[f'Операция {count}'] = f'Снятие {take_bank(check_bank())} руб,' \
                                                   f'Время операции: {datetime.datetime.now().strftime("%d.%m.%y %T")}'

        elif action == 2:
            operations_dict[f'Операция {count}'] = f'Пополнение {add_bank(check_bank())} руб, ' \
                                                   f'Время операции: {datetime.datetime.now().strftime("%d.%m.%y %T")}'
        elif action == 3:
            print("Всего доброго")
            print('Все операции : ')
            for key, val in operations_dict.items():
                print(f'{key}: {val}')
            break


bancomat()
