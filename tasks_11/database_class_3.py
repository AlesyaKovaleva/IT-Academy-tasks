"""
Задача 3
Реализовать программу с базой учащихся группы (данные хранятся в файле).
Записи по учащемуся должны быть представлены отдельным классом с полями:
имя, фамилия, пол, возраст. Программа должна предусматривать поиск по
одному или нескольким полям базы. Результат выводить в удобочитаемом виде
с порядковым номером записи. Скрипт программы должен принимать параметр,
который определяет формат хранения и реализации БД: в текстовом файле с
определенной структурой; в файле json.
"""

import json
import sys
import os


class BaseDB:
    db = []

    def __init__(self, filename):
        self.filename = filename
        self.db = self.load(filename)

    def load(self, filename):
        raise NotImplementedError

    def find(self, search):
        criteria = set(search)
        students_list = []

        for student_id, student in enumerate(self.db, 1):
            values = set(student.values())
            if criteria.issubset(values):
                students_list.append((student_id, student))
        return students_list


class TextDB(BaseDB):
    def load(self, filename):
        students = []
        with open(filename, encoding='utf-8') as f:
            for line in f:
                data = line.rstrip('\n').split(',')
                students.append(Student(*data))
        return students


class JsonDB(BaseDB):
    def load(self, filename):
        students = []
        with open(filename, encoding='utf-8') as f:
            student_list = json.loads(f.read())
            for student in student_list:
                students.append(
                    Student(student['name'], student['surname'], student['gender'], student['age'])
                )
        return students


class Student:
    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

    def values(self):
        return [
            self.name, self.surname, self.gender, self.age
        ]

    def __str__(self):
        return ' '.join(self.values())


choose_db = {
    'json': JsonDB,
    'txt': TextDB,
}


def make_list_student(file):
    if not os.path.isfile(file):
        return None

    extension = file.split('.')[-1]
    return choose_db[extension](file)


def print_search(student_list):
    if student_list:
        for student_id, student in student_list:
            print('Student № {}: {}'.format(student_id, student))
    else:
        print('Not found')


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Enter file name')
        return

    db = make_list_student(filename)
    if db is None:
        print('File not found')
        return

    while True:
        search_criteria = input('\nEnter the criteria to search for the student:\n'
                                '(if there are several criteria, enter them through &): ')

        if not search_criteria:
            break
        else:
            search_criteria = search_criteria.split('&')

        result = db.find(search_criteria)
        print_search(result)


if __name__ == '__main__':
    main()
