"""
2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


def to_hex(number: int):
    voc_to_check = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', }
    divisor = 16
    result = ''
    while number > 0:
        if number % divisor in voc_to_check.keys():
            result = voc_to_check[number % divisor] + result
        else:
            result = str(number % divisor) + result

        number = number // divisor

    print(result)


to_hex(1000)
print(hex(1000)[2:])


"""
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
import fractions
from math import gcd

def numerator_denominator(numerator: int, denominator: int):
    while gcd(numerator, denominator) > 1:
        gccd = gcd(numerator, denominator)
        numerator = numerator // gccd
        denominator = denominator // gccd
    return [numerator, denominator]



a, b = map(int, input('Введите дробь 1 в формате a/b: ').split('/'))
c, d = map(int, input('Введите дробь 2 в формате a/b: ').split('/'))
operator = input('Введите действие с дробями + или *: ')

if operator == '+':
    numerator, denominator = (a * d) + (c * b), b * d
else:
    numerator, denominator = a * c, b * d


lst = numerator_denominator(numerator, denominator)
numerator, denominator = lst[0], lst[1]

if numerator//denominator > 0 and not numerator % denominator:
    print(numerator//denominator)
else:
    print(f'{numerator}/{denominator}')

print(fractions.Fraction(4, 2) * fractions.Fraction(4, 2))

