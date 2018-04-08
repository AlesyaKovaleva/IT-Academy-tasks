"""
Задача 1
Дано натуральное число N. Выведите все его цифры по одной,
в обратном порядке, разделяя их пробелами или новыми строками.
При решении этой задачи нельзя использовать строки, списки,
массивы (ну и циклы, разумеется).
Разрешена только рекурсия и целочисленная арифметика.
"""


def output_number(number):
    if number < 0:
        number = abs(number)

    result = number // 10
    mod = number % 10

    if result == 0:
        return mod

    return '%s,%s' % (mod, output_number(result))


# print(output_number(0))


def test_output_number():
    number = 1234567890
    result = output_number(number)

    if result == '0,9,8,7,6,5,4,3,2,1':
        print('Test Ok')
    else:
        print('Test not Ok')


def test_output_number_1():
    number = 0
    result = output_number(number)

    if result == 0:
        print('Test Ok')
    else:
        print('Test not Ok')


def test_output_number_2():
    number = -31337
    result = output_number(number)

    if result == '7,3,3,1,3':
        print('Test Ok')
    else:
        print('Test not Ok')


test_output_number()
test_output_number_1()
test_output_number_2()
