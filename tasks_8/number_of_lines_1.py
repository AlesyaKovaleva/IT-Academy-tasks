"""
Задача 1
В текстовом файле посчитать количество строк, а также для каждой
отдельной строки определить количество в ней символов и слов.
"""

with open('my_file.txt', encoding='utf-8') as f:

    lines = 0
    symbols = 0
    words = 0

    for rows in f:
        lines += 1
        symbols = len(rows)
        words = len(rows.split())

        print('В {}й строке - символов: {}, слов: {}'.format(lines, symbols, words))
