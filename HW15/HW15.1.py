import logging
import argparse


def abs_path(abs_path: str) -> tuple:
    result = []
    result.append(abs_path)
    for_result = abs_path.split('\\')
    result.append(for_result[-1])
    for_result2 = for_result[-1].split('.')
    result.append(for_result2[-1])
    logging.basicConfig('path.log', 'a', encoding='utf-8', level=logging.DEBUG)
    logging.info(str(result))
    return tuple(result)


my_string = r"D:\GeekBrains\Python_SPECIFICATION\HW15\test.py"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсер для определения пути к файлу, файла и его расширения')
    parser.add_argument('path', metavar='path for file', type=str, nargs='+', help='Enter path')
    args = parser.parse_args()
    print(abs_path(*args.path))