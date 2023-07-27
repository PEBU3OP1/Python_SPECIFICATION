"""
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

"""
import csv
import json
import random
from functools import wraps
from os.path import isfile


def read_csv(name:str = 'default.csv'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(name, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i > 0:
                        args = (complex(j) for j in row)
                        res = func(*args, **kwargs)
                        yield res

        return wrapper
    return decorator

def save_to_json(func):

    def wrapper(*args, **kwargs):
        if isfile(f'{func.__name__}.json'):
            with open(f'{func.__name__}.json', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
        for result in func(*args, **kwargs):
            if result:
                data.append({'args': args, 'kwargs': kwargs, 'result': str(result)})
        with open(f'{func.__name__}.json','w', encoding='utf-8') as f:
            json.dump(data, f)
    return wrapper



def csv_file_generation(name: str = 'default', rows_qty: int = random.randint(100, 1000)):
    list_of_rows = []
    for _ in range(rows_qty):
        a, b, c = random.sample(range(-100, 100), 3)
        list_of_rows.append({'a': a, 'b': b, 'c': c})

    with open(f'{name}.csv', mode='w', encoding='utf-8', newline='')as f:
        writer = csv.DictWriter(f, fieldnames=['a', 'b', 'c'])
        writer.writeheader()
        writer.writerows(list_of_rows)

@save_to_json
@read_csv()
def quadratic_equation(a: complex, b: complex, c: complex):
    if a != 0:
        d: complex = b ** 2 - 4 * a * c
        x1: complex = (-b + d ** 0.5) / (2 * a)
        x2: complex = (-b - d ** 0.5) / (2 * a)
        return d, x1, x2
    return

quadratic_equation()