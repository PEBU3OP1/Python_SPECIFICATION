import re
abs_path = r'D:\PycharmProjects\Database\Pricelist\Колеса\Диски_колесные.csv'


def split_path(path: str) -> tuple:
    return(path[:path.rfind('\\')], *path[path.rfind('\\'):].split('.'))

print(split_path(abs_path))
