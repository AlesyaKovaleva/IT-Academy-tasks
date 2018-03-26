"""
Задача 2
В текстовый файл построчно записаны фамилия и имя учащихся класса и
его оценка за контрольную. Вывести на экран всех учащихся, чья
оценка меньше 3 баллов и посчитать средний балл по классу.
"""

expected_mark = int(input('Введите оценку: '))

with open('my_file.txt', encoding='utf-8') as f:

    count = 0
    sum_mark = 0

    for text in f:
        mark = int(text.split()[-1])
        sum_mark += mark
        count += 1

        if mark < expected_mark:
            print(text[:-1])

    print('Средний балл по классу: {}'.format(sum_mark / count))
