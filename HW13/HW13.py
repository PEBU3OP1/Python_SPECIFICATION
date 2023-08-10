
"""
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины.
"""
"Классы исключения для 3 разных задач"
class ValError(Exception):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a <= 0 and self.b <= 0:
            return f"Ошибка ввода: обе стороны имеют невалидные значения = {self.a}; {self.b}"

        elif self.a == self.a or self.b == self.b:
            return 'Значение одной из сторон 0!'
        else:
            if self.a <= 0:
                return f"Ошибка ввода: сторона имеет невалидное  значение = {self.a} "
            else:
                return f"Ошибка ввода: сторона имеет невалидное  значение  = {self.b}"


class ValFormatError(Exception):
    def __init__(self, operation: str):
        self.operation = operation

    def __str__(self):
        if self.operation == '+':
            return f"Error: Невозможно сложить матрицы, матрицы разных размеров"
        elif self.operation == '*':
            return f"Error: Невозможно перемножить матрицы: не подходят размерности"
        else:
            return f"Error: Невозможно сравнить. Матрицы разных размеров"


class ValueBankError(Exception):
    def __init__(self, cash):
        self.cash = cash

    def __str__(self):
        return f"Ошибка ввода. Число {self.cash} < 0 "



"""Example"""


class Rectangle:

    def __init__(self, a:int, b: int):
        self.a = a
        self.b = b

    def perimetr(self):
        return 2*self.a + 2*self.b

    def __add__(self, other):
        return Rectangle((self.a + other.a), (self.b + other.b))

    def __sub__(self, other):
        if self.a == other.a:
            raise ValError(self.a, other.a)
        elif self.b == other.b:
            raise ValError(self.b, other.b)
        return Rectangle(abs(self.a - other.a),abs(self.b - other.b))

    def __lt__(self, other):
        return self.perimetr() < other.perimetr()
    def __gt__(self, other):
        return self.perimetr() > other.perimetr()
    def __eq__(self, other):
        return self.perimetr() == other.perimetr()
    def __ne__(self, other):
        return self.perimetr() != other.perimetr()

a = Rectangle(2,3)
b = Rectangle(1,3)

c = a-b #__main__.ValError: Значение одной из сторон 0!