"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""


import math


class Circle:
    def __init__(self, rad):
        self.rad = rad

    def square_circle(self):
        s = math.pi * self.rad**2
        return s
    def length_circle(self):
        l = 2 * math.pi*self.rad
        return l

"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Bird(Animal):
    def __init__(self,name, age, color):
        self.name = name
        self.age = age
        self.color = color
        super().__init__(name,age)


class Cat(Animal):
    def __init__(self, name, age, jump):
        self.name = name
        self.age = age
        self.jump = jump
        super().__init__(name, age)

class Cow(Animal):
    def __init__(self, name, age, milk):
        self.name = name
        self.age = age
        self.milk  = milk
        super().__init__(name, age)