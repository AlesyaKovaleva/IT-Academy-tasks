"""
Задача 3
Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы.
Результат выводить в удобочитаемом виде с порядковым номером записи.
"""
import sys
sys.path.append("..")

from tasks_5.student_database_3 import search_student, print_search


def make_student(name, surname, gender, age):
    return {
        'name': name,
        'surname': surname,
        'gender': gender,
        'age': age,
    }


def make_list_students():
    students_list = []

    with open('my_file.txt', encoding='utf-8') as f:
        for line in f:
            data = line.rstrip('\n').split(',')
            students_list.append(make_student(*data))
    return students_list


def main():
    search_criteria = input('Enter the criteria to search for the student:\n'
                            '(if there are several criteria, enter them through &): ').split('&')

    print_search(search_student(make_list_students(), search_criteria))


# if __name__ == '__main__':
#     main()


def test_make_student():
    result = make_student('Иван', 'Иванов', 'мужской', 32)
    if result == {
        'name': 'Иван',
        'surname': 'Иванов',
        'gender': 'мужской',
        'age': 32,
    }:
        print('Test Ok')
    else:
        print('Test not Ok')


def test_make_list_students():
    result = make_list_students()

    if result == [{'name': 'Петр', 'surname': 'Петров', 'gender': 'мужской', 'age': '23'},
                  {'name': 'Сидор', 'surname': 'Сидоров', 'gender': 'мужской', 'age': '32'},
                  {'name': 'Анна', 'surname': 'Каренина', 'gender': 'женский', 'age': '21'},
                  {'name': 'Оби', 'surname': 'ван Кеноби', 'gender': 'мужской', 'age': '32'},
                  {'name': 'Лара', 'surname': 'Крофт', 'gender': 'женский', 'age': '21'}]:
        print('Test Ok')
    else:
        print('Test not Ok')


# test_make_student()
# test_make_list_students()
