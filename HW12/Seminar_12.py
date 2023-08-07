"""
Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.

Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл
"""
from collections import deque as dq
import json

# class Factorial():
#     def __init__(self, k: int):
#         self.k = dq(maxlen=k)
#         self.val = dq(maxlen=k)
#
#     def __call__(self, value):
#         res = 1
#         for i in range(1, value+1):
#             res *= i
#         self.k.append(res)
#         self.val.append(value)
#         return self
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         with open('result.json', mode='w', encoding='utf-8') as js:
#             json.dump(str(self), js)
#     def __str__(self):
#
#         return str({self.val[i]: self.k[i] for i in range(len(self.k))}  )
#
# with Factorial(2) as k:
#     print(k(5))
#     print(k(7))



"""
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class Factorial():
    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.result = 1
        for i in range(1, self.start):
            self.result *= i

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            for i in range(self.start, self.stop, self.step):
                self.result *= self.start
                self.start += self.step
                return self.result
        else:
            raise StopIteration