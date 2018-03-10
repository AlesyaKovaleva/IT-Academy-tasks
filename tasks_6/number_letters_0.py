"""
Задача 0
Написать программу, запрашивающую у пользователя строку с текстом и разделитель.
Необходимо вывести список слов с их длиной в начале слова, например, 5hello.
Для каждой из пользовательских функций написать функцию-тест.
"""


def read_user_data():

    text = input("Введите текст: ")
    separator = input("Введите разделитель: ")

    while True:
        if text == '':
            text = input("Вы не ввели текст! Введите текст: ")
        elif separator == '':
            separator = input("Вы не ввели разделитель! Введите разделитель: ")
        else:
            break

    return text, separator


def count_letters(text, separator):
    result = text.split(separator)
    filter_result = list(filter(lambda x: x != '', result))
    result_text = list(map(lambda x: str(len(x)) + x, filter_result))
    return ', '.join(result_text)


# print(count_letters(*read_user_data()))


def test_count_letters_1():
    text = 'The@Force@is@with@me'
    separator = '@'
    if count_letters(text, separator) == '3The, 5Force, 2is, 4with, 2me':
        print('Test is OK')
    else:
        print('Test is not Ok')


def test_count_letters_2():
    text = 'And I am with the Force.'
    separator = ' '
    if count_letters(text, separator) == '3And, 1I, 2am, 4with, 3the, 6Force.':
        print('Test is OK')
    else:
        print('Test is not Ok')


def test_count_letters_3():
    text = '.|And|I| fear| nothing.| '
    separator = '|'
    if count_letters(text, separator) == '1., 3And, 1I, 5 fear, 9 nothing., 1 ':
        print('Test is OK')
    else:
        print('Test is not Ok')


def test_count_letters_4():
    text = 'For all is as the Force wills it.'
    separator = 'l'
    if count_letters(text, separator) == '5For a, 19 is as the Force wi, 5s it.':
        print('Test is OK')
    else:
        print('Test is not Ok')


def test_count_letters_5():
    text = '&&&'
    separator = '&'
    if count_letters(text, separator) == '':
        print('Test is OK')
    else:
        print('Test is not Ok')


test_count_letters_1()
test_count_letters_2()
test_count_letters_3()
test_count_letters_4()
test_count_letters_5()
