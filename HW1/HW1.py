"""
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с
суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным
или равносторонним.
# """

def triangle_check()-> None:
    while True:
        try:
            a = int(input("Введите длину стороны a, см: "))
            b = int(input("Введите длину стороны b, см: "))
            c = int(input("Введите длину стороны c, см: "))

            if a + b < c or b + c < a or a + c < b:
                print("Неверные параметры треугольника")
            elif a == b and b == c:
                print("Треуголник равносторонний")
            elif a == b or b == c or a == c:
                print("Данный треугольник равнобедренный")
            else:
                print("Данный треугольник разносторонний")
            break
        except ValueError:
            continue


triangle_check()

"""
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


def simple_check(number: int) -> bool:
    flag = True
    check_list = [2, 3, 5, 7]

    if number in check_list:
        return flag

    for i in check_list:
        if not number % i:

            flag = False
    return flag


def simple_or_not():
    while True:
        try:
            number = int(input("Введите число и мы проверим простое ли оно: "))
            if number < 0 or number > 100_000:
                print("Число не в диапазоне от 0 до 100 000!")
                continue
            elif number == 1:
                print("Это 1. Оно ни простое ни составное")
                break

            if simple_check(number):
                print("Число простое!")
            else:
                print("Число составное!")
            break
        except ValueError:
            continue

simple_or_not()
