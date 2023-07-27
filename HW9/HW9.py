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

def create_guess_game(answer:int):
    def guess_game (attemts:int):
        for _ in range(attemts):
            guess = int(input('Отгадайте число: '))
            if guess == answer:
                print('Bingo!')
                return
            elif guess < answer:
                print('Number is more')
            else:
                print('Number is less')
        print('Looser!')
    return guess_game

num = create_guess_game(5)
num(3)

"""
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""

import random
def check_data(func):
    def wrapper(answer:int, attempts:int):
        if not answer :
            print('New answer')
            answer = random.randint(1,100)
        if not attempts:
            print('New attemts')
            attempts = random.randint(1,10)
        return func(answer,attempts)
    return wrapper


@check_data
def create_guess_game(answer:int, attemts:int):
    def guess_game ():
        for _ in range(attemts):
            guess = int(input('Отгадайте число: '))
            if guess == answer:
                print('Bingo!')
                return
            elif guess < answer:
                print('Number is more')
            else:
                print('Number is less')
        print('Looser!')
    return guess_game()

create_guess_game(0,10)
