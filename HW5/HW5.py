"""
1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
abs_path = r'D:\PycharmProjects\Database\Pricelist\Колеса\Диски_колесные.csv'


def split_path(path: str) -> tuple:
    return(path[:path.rfind('\\')], *path[path.rfind('\\'):].split('.'))

print(split_path(abs_path))

"""
 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
 имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь 
 с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка 
 умноженная на процент премии"""

names = ['Анатолий', 'Онотолий', 'Онотоле', 'Анатоль']
salary = [3500, 2300, 11000, 100]
bonus = ['10.25%', '15.1%', '18.2%', '12.3%']


def prize_calc(names: list, salary: list, bonus: list) -> dict:
   return dict(zip(names, map(lambda x, y: (float(x[:-1])/100)*y, bonus, salary)))



print(prize_calc(names, salary, bonus))

"""
3.  Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(10)))