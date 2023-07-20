"""
1. Напишите функцию группового переименования файлов. Она должна:
  - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
  - принимать параметр количество цифр в порядковом номере.
  - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
  - принимать параметр расширение конечного файла.
  - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы
с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.

3.Соберите из созданных на уроке и в рамках домашнего задания
функций пакет для работы с файлами.
"""
import random
from os import listdir, rename
from os.path import isfile, join

def group_rename(new_name:str, final_extension:str, extension_of_files:str,miin =0, maax =0,needed_files_qty = 10,
                 digit_number=0):

    path = 'D:\GeekBrains\Python_SPECIFICATION\HW7\Folder_to_test'
    count = 0
    file_count = 0




    onlyfiles = [file for file in listdir(path) if isfile(join(path, file))]

    for file in onlyfiles:
        if extension_of_files == file[file.rfind('.') + 1:]:
            file_count += 1
            count += 1
            if miin or maax:
                name1 = file[:file.rfind('.')][miin:maax]
            else:
                name1 = ''

            digit_in_name = (len(str(digit_number)) - len(str(count)) if len(str(digit_number)) > len(str(count)) else 0)
            final_new_name = name1 + new_name + (digit_in_name * '0')+str(count)
            rename(f'{path}\{file}', f'{path}\{final_new_name}.{final_extension}')
            if file_count == needed_files_qty:
                break

