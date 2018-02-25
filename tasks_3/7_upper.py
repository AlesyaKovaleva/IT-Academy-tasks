"""
Задача 7
Пользователь вводит строку и символ.
В строке найти все вхождения этого символа и перевести его
в верхний регистр, а также удалить часть строки, начиная
с последнего вхождения этого символа и до конца.
"""

string = input("Введите строку: ")
symbol = input("Введите символ: ")

replaced_string = string.replace(symbol, symbol.upper())
last_index = replaced_string.rfind(symbol.upper())
total_row = replaced_string[:last_index]

print(total_row)
