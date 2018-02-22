"""
Написать программу, которая выводит три переменные first_name,
last_name, patronymic разделенные ‘|' (прямой чертой).
Например “Иван|Иванович|Иванов“.

Алгоритм: goo.gl/qTgZYn
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
patronymic = input("Enter your patronymic: ")

print(first_name, last_name, patronymic, sep="|")
