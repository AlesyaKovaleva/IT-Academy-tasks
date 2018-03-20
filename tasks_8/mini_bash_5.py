"""
Задача 5*
Реализовать программу, позволяющую осуществлять управление файлами:
копирование, создание, удаление, переименование.
Необходимо предусмотреть возможность смен директории.
Изначально используется текущий каталог запуска скрипта программы.
"""

import os
import sys
import shutil


def show_help(*args):
    print("""
    help  - list of commands
    pwd   - present working directory
    ls    - list directory content
    mkdir - make directory
    touch - make file
    cd    - change directory
    cp    - copy file or directory
    rm    - remove file or directory
    mv    - move file or directory
    exit
    """)


def present_working_directory(*args):
    path = os.getcwd()
    print(path)


def list_directory_content(*args):
    content = os.listdir(path=".")
    for file in content:
        print(file)


def make_directory(arguments):
    path = os.getcwd()
    for directory in arguments:
        try:
            os.mkdir(os.path.join(path, directory))
        except FileExistsError:
            print(directory, '- такая директория уже существует')


def touch(arguments):
    path = os.listdir(path=".")
    for file in arguments:
        if file in path:
            print(file, '- такой файл уже существует')
        else:
            new_file = open(file, 'w')
            new_file.close()


def change_directory(arguments):
    if len(arguments) > 1:
        print('Введено неверное количество аргументов.')
        return

    if arguments[0] == '..' or os.path.isdir(arguments[0]):
        os.chdir(arguments[0])
    else:
        print('Такого каталога не существует')


def copy_file_and_directory(arguments):
    if len(arguments) > 2:
        print('Введено неверное количество аргументов.')
        return

    if not os.path.exists(arguments[0]):
        print('Такого объекта не существует')

    if os.path.isdir(arguments[0]):
        if os.path.isfile(arguments[1]):
            print('Невозможно скопировать каталог в файл.')
            return

        if os.path.isdir(arguments[1]):
            cwd = os.getcwd()
            os.chdir(arguments[1])
            shutil.copytree(
                os.path.join(cwd, arguments[0]),
                arguments[0]
            )
            os.chdir(cwd)
        else:
            shutil.copytree(arguments[0], arguments[1])
    else:
        shutil.copy(arguments[0], arguments[1])


def remove_file_and_directory(arguments):
    if len(arguments) > 1:
        print('Введено неверное количество аргументов.')
        return

    if not os.path.exists(arguments[0]):
        print('Такого объекта не существует')
        return

    if os.path.isdir(arguments[0]):
        shutil.rmtree(arguments[0])
    else:
        os.remove(arguments[0])


def move_file_and_directory(arguments):
    if len(arguments) > 2:
        print('Введено неверное количество аргументов.')
        return

    if not os.path.exists(arguments[0]):
        print('Такого объекта не существует')
    else:
        shutil.move(arguments[0], arguments[1])


commands = {
    'help': show_help,
    'pwd': present_working_directory,
    'ls': list_directory_content,
    'mkdir': make_directory,
    'touch': touch,
    'cd': change_directory,
    'cp': copy_file_and_directory,
    'rm': remove_file_and_directory,
    'mv': move_file_and_directory,
}


def main():
    while True:
        command_input = input('> $ ').split(' ')
        command = command_input[0]
        arguments = command_input[1:]

        if command == 'exit':
            sys.exit()

        if command in commands:
            func = commands[command]
            func(arguments)
        else:
            print('Такой команды не существует.')


if __name__ == '__main__':
    main()
