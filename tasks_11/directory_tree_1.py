"""
Задача 1
Реализовать программу, которая отображает дерево каталогов.
Путь к целевому каталогу запрашивается у пользователя.
В программе не должно использоваться циклов.
Вывод результата программы должен быть следующего вида:
|__ Folder 1
|___ Folder 2
|___ File 2.1
|___ File 2.2
|__ File 1.1
|__ File 1.2
"""

import os

path = input('Введите путь к каталогу: ')


def list_files(path, indent=2, file_print=None):
    if not os.path.isdir(path):
        print('Такого каталога не существует.', file=file_print)
        return

    for root, dirs, files in os.walk(path):
        for directory in dirs:
            print('|' + '_' * indent, directory, file=file_print)
            directory = os.path.join(root, directory)
            list_files(directory, indent=indent + 2, file_print=file_print)

        for file in files:
            print('|' + '_' * indent, file, file=file_print)


with open('dirs.txt', 'w', encoding='utf-8') as f:
    list_files(path, file_print=f)
