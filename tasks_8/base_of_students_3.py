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


def main():
    students_list = []
    search_criteria = input('Enter the criteria to search for the student:\n'
                            '(if there are several criteria, enter them through &): ').split('&')

    with open('my_file.txt', encoding='utf-8') as f:
        for line in f:
            data = line.rstrip('\n').split(',')
            students_list.append(make_student(*data))

    print_search(search_student(students_list, search_criteria))


if __name__ == '__main__':
    main()
