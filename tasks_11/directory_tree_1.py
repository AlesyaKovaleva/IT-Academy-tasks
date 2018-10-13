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


def print_dir(dirs, indent=0, file_print=None, root=None):

    if not dirs:
        return

    path = dirs[0]
    rest = dirs[1:]

    realpath = os.path.abspath(path) if not root else os.path.join(root, path)

    path = os.path.basename(realpath)

    out_template = '%s' if not root else '├' + '─' * indent + ' %s'

    if os.path.isdir(realpath):
        print(out_template % path, file=file_print)
        print_dir(os.listdir(realpath), indent=indent + 2, file_print=file_print, root=realpath)

    if os.path.isfile(realpath):
        print(out_template % path, file=file_print)

    if rest:
        print_dir(rest, indent=indent, root=root)


print_dir([path])
