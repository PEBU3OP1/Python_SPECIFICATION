"""
                                                    Cеминар
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
 - от 1 до 100 для загадывания,
 - от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.

"""

# def create_guess_game(answer:int):
#     def guess_game (attemts:int):
#         for _ in range(attemts):
#             guess = int(input('Отгадайте число: '))
#             if guess == answer:
#                 print('Bingo!')
#                 return
#             elif guess < answer:
#                 print('Number is more')
#             else:
#                 print('Number is less')
#         print('Looser!')
#     return guess_game
#
# num = create_guess_game(5)
# num(3)
from functools import wraps

"""
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""

# import random
# def check_data(func):
#     def wrapper(answer:int, attempts:int):
#         if not answer :
#             print('New answer')
#             answer = random.randint(1,100)
#         if not attempts:
#             print('New attemts')
#             attempts = random.randint(1,10)
#         return func(answer,attempts)
#     return wrapper
#
#
# @check_data
# def create_guess_game(answer:int, attemts:int):
#     def guess_game ():
#         for _ in range(attemts):
#             guess = int(input('Отгадайте число: '))
#             if guess == answer:
#                 print('Bingo!')
#                 return
#             elif guess < answer:
#                 print('Number is more')
#             else:
#                 print('Number is less')
#         print('Looser!')
#     return guess_game()
#
# create_guess_game(0,10)


""""
Задание №3
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
возвращает. 
    - При повторном вызове файл должен расширяться, а не перезаписываться.
    - Каждый ключевой параметр сохраните как отдельный ключ json словаря.
    - Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
    - Имя файла должно совпадать с именем декорируемой функции.
"""
# import json
# from os.path import isfile
#
# def save_to_json(func):
#     def wrapper(*args, **kwargs):
#         if isfile(f'{func.__name__}.json'):
#             with open(f'{func.__name__}.json', encoding='utf-8') as f:
#                 data = json.load(f)
#         else:
#             data = []
#         result = func(*args, **kwargs)
#         data.append({'args': args, 'kwargs':kwargs, 'result':result})
#         with open(f'{func.__name__}.json','w', encoding='utf-8') as f:
#             json.dump(data, f)
#     return wrapper
#
# @save_to_json
# def func(*args, **kwargs):
#     return sum(args)
#
# func(15,20, c = 1, y=55)

"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.
"""

# def count(num):
#     def run_func(func):
#         def wrapper(*args,**kwargs):
#             res = 0
#             for _ in range(num):
#                 res += func(*args, **kwargs)
#             return res
#         return wrapper
#     return run_func
#
# @count(5)
# def func(*args, **kwargs):
#
#     return sum(args)
#
#
# print(func(2))


"""
Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
    - декораторами для сохранения параметров,
    - декоратором контроля значений и
    - декоратором для многократного запуска.
Выберите верный порядок декораторов.

"""

# import random
# from os.path import isfile
# import json
#
#
#
# def count(num):
#     def run_func(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             for _ in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return run_func
#
#
# def save_to_json(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if isfile(f'{func.__name__}.json'):
#             with open(f'{func.__name__}.json', encoding='utf-8') as f:
#                 data = json.load(f)
#         else:
#             data = []
#         result = func(*args, **kwargs)
#         data.append({'args': args, 'kwargs':kwargs, 'result':result})
#         with open(f'{func.__name__}.json','w', encoding='utf-8') as f:
#             json.dump(data, f)
#     return wrapper
#
#
# def check_data(func):
#     @wraps(func)
#     def wrapper(answer:int, attempts:int):
#         if not answer :
#             print('New answer')
#             answer = random.randint(1,100)
#         if not attempts:
#             print('New attemts')
#             attempts = random.randint(1,10)
#         return func(answer,attempts)
#     return wrapper
#
# @count(2)
# @save_to_json
# @check_data
# def create_guess_game(answer:int, attemts:int):
#     def guess_game ():
#         for _ in range(attemts):
#             guess = int(input('Отгадайте число: '))
#             if guess == answer:
#                 print('Bingo!')
#                 return answer
#
#             elif guess < answer:
#                 print('Number is more')
#             else:
#                 print('Number is less')
#         print('Looser!')
#
#     return guess_game()
#
# create_guess_game(3,20)