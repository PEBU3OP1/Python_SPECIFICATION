"""
Семинар5

1. Пользователь вводит строку из четырех или более целых чисел, разделенных символом /

    Сформируйте словарь, где
        - второе и третье число являются ключами
        - первое число является значением для первого ключа
        - четвертое и все последующие числа хранятся в кортеже, как второй ключ
"""

msg = '12/22/23/4/5/6/7'
def dict_from_str(msg:str):
    a,b,c,*d = msg.split("/")
    return {b:a, c:tuple(d)}

print(dict_from_str(msg))

"""
2. Самостоятельно сохраните в переменной строку текста. Создайте из строки словарь, где ключ - буква, 
а значение код буквы.
"""

msg = 'fadghnm+tyiu'
my_dict = {i: ord(i) for i in msg}


"""
возьмите словарь. Сохраните его в итератор. Далее выведите первые 5 пар ключ значение, 
обращаясь к итератору, а не к словарю
"""
my_iter = iter(my_dict.items())
for _ in range(5):
    print(next(my_iter))

"""
3. Создайте генератор четных чисел от 0 до 100. Из последовательности исключите числа, сумма цифр которых == 8
"""
my_gen = (i for i in range(101) if not i%2 and sum(map(int, str(i))) != 8)
print(list(my_gen))

"""
4. Напишите программу, которая выводит на экран числа от 1 до 100.
   При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
   Вместо чисел, кратных пяти — слово «Buzz».
   Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
   *Превратите решение в генераторное выражение.
"""

llds = ('FizzBuzz' if not i%3 and not i%5 else 'Fizz' if not i%3 else 'Buzz' if not i%5 else i for i in range(1,101))
for _ in iter(llds):
    print(next(llds))

for i in range(1,101):
    if not i%3 and not i%5:
        i = 'FizzBuzz'
    elif not i%3:
        i = 'Fizz'
    elif not i%5:
        i = 'Buzz'
    print(i)


"""6.Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
     Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
     Для вывода результата используйте «принт» без перехода на новую строку.
"""

for i in range(2, 10):

    for j in range(2, 6):
        print(f'{j} x {i} = {i * j}', end='\t')
    print()

print()

for i in range(2, 10):
    for j in range(6, 10):
        print(f'{j} x {i} = {i * j}', end='\t')
    print()

my_gen = (print(f'{i} x {j} = {i * j}') for i in range(2,10) for j in range(2,11))

# while True:
#     next(my_gen)


"""
7. Создайте функцию-генератор.
   Функция генерирует N простых чисел, начиная с числа 2.
   Для проверки числа на простоту используйте правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def my_gen(n):
    for i in range (2, n+1):
        for j in range(2, int((n**0.5))+1):
            if i%j == 0:
                break
            yield i

print(set(my_gen(15)))

def gen_simple(n: int):
    count = 0
    start = 2
    while count < n:
        flag = False
        start += 1
        for i in range(2, start):
            if start % i == 0 and start!=i:
                flag = True

        if not flag:
            yield start
            count+=1

print(list(gen_simple(10)))


"""
ДЗ
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
