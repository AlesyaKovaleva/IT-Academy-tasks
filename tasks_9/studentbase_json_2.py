"""
Задача 2
Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся: имя, фамилия, пол, возраст. Программа должна
предусматривать поиск по одному или нескольким полям базы. Результат
выводить в удобочитаемом виде с порядковым номером записи. Скрипт программы
должен принимать параметр, который определяет формат хранения и реализации
БД: в текстовом файле с определенной структурой; в файле json.
"""
import json
import os
import sys
sys.path.append("..")

from tasks_5.student_database_3 import search_student, print_search
from tasks_8.base_of_students_3 import make_list_students


def make_list_student(file):
    if not os.path.isfile(file):
        return None

    if file.endswith('json'):

        with open(file, encoding='utf-8') as f:
            data = json.loads(f.read())
            return data

    elif file.endswith('txt'):
        return make_list_students(file)


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Enter file name')
        return

    students = make_list_student(filename)
    if students is None:
        print('File not found')
        return

    search_criteria = input('Enter the criteria to search for the student:\n'
                            '(if there are several criteria, enter them through &): ').split('&')

    print_search(search_student(students, search_criteria))


# if __name__ == '__main__':
#     main()


def test_make_list_student():
    result = make_list_student('my_file.json')

    if result == [{'name': 'Петр', 'surname': 'Петров', 'gender': 'мужской', 'age': '23'},
                  {'name': 'Сидор', 'surname': 'Сидоров', 'gender': 'мужской', 'age': '32'},
                  {'name': 'Анна', 'surname': 'Каренина', 'gender': 'женский', 'age': '21'},
                  {'name': 'Оби', 'surname': 'ван Кеноби', 'gender': 'мужской', 'age': '32'},
                  {'name': 'Лара', 'surname': 'Крофт', 'gender': 'женский', 'age': '21'}]:
        print('Test Ok')
    else:
        print('Test not Ok')


def test_make_list_student_1():
    result = make_list_student('my_file.txt')

    if result == [{'name': 'Петр', 'surname': 'Петров', 'gender': 'мужской', 'age': '23'},
                  {'name': 'Сидор', 'surname': 'Сидоров', 'gender': 'мужской', 'age': '32'},
                  {'name': 'Анна', 'surname': 'Каренина', 'gender': 'женский', 'age': '21'},
                  {'name': 'Оби', 'surname': 'ван Кеноби', 'gender': 'мужской', 'age': '32'},
                  {'name': 'Лара', 'surname': 'Крофт', 'gender': 'женский', 'age': '21'}]:
        print('Test Ok')
    else:
        print('Test not Ok')


test_make_list_student()
test_make_list_student_1()
