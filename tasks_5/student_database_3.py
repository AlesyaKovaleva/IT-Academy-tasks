"""
Задача 3
Реализовать программу с базой учащихся группы.
Записи по учащемуся: имя, фамилия, пол, возраст.
Программа должна предусматривать поиск по одному или нескольким полям базы.
Результат выводить в удобочитаемом виде с порядковым номером записи.
"""

student_database = [{'surname': 'Ivanov', 'name': 'Petr', 'gender': 'male', 'age': '22'},
                    {'surname': 'Petrov', 'name': 'Ivan', 'gender': 'male', 'age': '31'},
                    {'surname': 'Dolgov', 'name': 'Pavel', 'gender': 'male', 'age': '25'},
                    {'surname': 'Medved', 'name': 'Lisa', 'gender': 'female', 'age': '31'}]

search_criteria = input('Enter the criteria to search for the student:\n'
                        '(if there are several criteria, enter them through &): ').split('&')


def search_student(database, search):
    criteria = set(search)
    students_list = []

    for id, student in enumerate(database, 1):
        values = set(student.values())
        if criteria.issubset(values):
            student['id'] = id
            students_list.append(student)
    return students_list


# def search_student(database, search):
#     criteria = set(search)
#     students_list = []
#
#     for index in range(len(database)):
#         student = database[index].copy()
#         values = set(student.values())
#         if criteria.issubset(values):
#             student['id'] = index + 1
#             students_list.append(student)
#     return students_list


def print_search(result_list):
    if result_list:
        for elements in result_list:
            print('\nStudent № {id}: {surname} {name} {gender} {age}'.format(**elements))
    else:
        print('Not found')


print_search(search_student(student_database, search_criteria))
