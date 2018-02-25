"""
Задача 8
Дан список кортежей
grades = [(‘Ann’, 9), (‘John’, 7), (‘Smith’, 5), (‘George’, 6)].
Вывести информацию об оценках по возрастанию в виде:
‘Hello Ann! Your grade is 9’
"""
# from operator import itemgetter

grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]

# grades.sort(key=itemgetter(1))
# grades.sort(key=lambda q: q[1])

for index in range(len(grades)):
    value = grades[index]
    grades_reverse = (value[1], value[0])
    grades[index] = grades_reverse

grades.sort()

for grade in grades:
    print("Hello {}! Your grade is {}.".format(grade[1], grade[0]))
