"""
Задача 4
Реализовать программу, которая выводит содержимое каталога в файловой системе.
Путь к каталогу запрашивается у пользователя.
"""

import os

path = input('Введите путь к каталогу: ')


def list_files(path, file_print=None):
    if not os.path.isdir(path):
        print('Такого каталога не существует.', file=file_print)
        return

    for root, dirs, files in os.walk(path):
        for directory in dirs:
            directory = os.path.join(root, directory)
            print(' ', directory, file=file_print)
            list_files(directory, file_print=file_print)

        for file in files:
            print('    ', file, file=file_print)


with open('dirs.txt', 'a', encoding='utf-8') as f:
    list_files(path, file_print=f)


# def list_files(path, indent=0, file=None):
#     if not os.path.isdir(path):
#         print('Такого каталога не существует.', file=file)
#         return
#
#     print(' ' * indent, path, file=file)
#     for item in os.listdir(path=path):
#         if not os.path.isdir(path + '/' + item):
#             print(' ' * (indent + 4), item, file=file)
#         else:
#             list_files(path + '/' + item, indent=indent + 4, file=file)
#
#
# with open('dirs.txt', 'a', encoding='utf-8') as f:
#     list_files(path, file=f)
