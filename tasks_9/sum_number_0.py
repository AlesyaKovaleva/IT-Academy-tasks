"""
Задача 0
Дано натуральное число N. Вычислите сумму его цифр.
При решении этой задачи нельзя использовать строки,
списки, массивы и циклы.
"""


def sum_numbers(number):

    if number < 0:
        number = abs(number)

    result = number // 10
    mod = number % 10

    if result == 0:
        return mod

    return mod + sum_numbers(result)


# print(sum_numbers(54))


def test_sum_numbers():
    number = 123
    result = sum_numbers(number)
    if result == 6:
        print('Test Ok')
    else:
        print('Test not Ok')


def test_sum_numbers_1():
    number = 0
    result = sum_numbers(number)
    if result == 0:
        print('Test Ok')
    else:
        print('Test not Ok')


def test_sum_numbers_2():
    number = -31337
    result = sum_numbers(number)
    if result == 17:
        print('Test Ok')
    else:
        print('Test not Ok')


test_sum_numbers()
test_sum_numbers_1()
test_sum_numbers_2()
