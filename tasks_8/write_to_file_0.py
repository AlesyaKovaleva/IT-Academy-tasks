"""Задача 0
Создать текстовый файл, записать в него построчно данные, которые
вводит пользователь. Окончанием ввода пусть служит пустая строка.
"""

with open('my_file.txt', 'a', encoding='utf-8') as f:

    while True:
        text = input('Введите текст: ')
        print(text, file=f)
        if text == '':
            break
