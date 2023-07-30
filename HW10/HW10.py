"""
Доработаем задачи 5-6. Создайте класс-фабрику.
    - Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
    - Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
"""
import random
from datetime import datetime

from Seminar10 import Cat,Cow,Bird


class factory_class:
    def __init__(self, classname, param1, param2,param3):
        self.classname = classname
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    def activate(self):
        return self.classname(self.param1, self.param2,self.param3)

p = factory_class(Cat, 'fds', 'fds', '33')

print(type(p.activate()))


"""
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.
"""

class HW6:
    def guess_game(min_num: int = random.randint(-100, 0), max_num: int = random.randint(0, 100),
                   attemts: int = random.randint(2, 15)) -> bool:
        guess_num = random.randint(min_num, max_num)
        while attemts > 0:
            print(f'Попыток: {attemts}')
            guess = int(input("Какое число? - "))
            if guess == guess_num:
                print('Bingo!')
                return True
            elif guess > guess_num:
                print('Меньше')
            else:
                print('Больше')
            attemts -= 1
        print(f'Вы проиграли, было загадано {guess_num}')
        return False

    def check_date(date: str) -> bool:

        day, month, year = map(int, date.split('.'))
        print(day, month, year)
        try:
            res = datetime(day=day, month=month, year=year)
            print(res)
            return True
        except:
            print('Неверная дата')
            return False

p = HW6
p.guess_game()