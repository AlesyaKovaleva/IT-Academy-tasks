"""
Написать программу, которая запрашивает имя пользователя ‘Enter your name: ’ и
выводит ‘Hello World! Hello Ivan!’. Вместо ‘Ivan’ вывести введенное значение.

Алгоритм: https://goo.gl/FVSeg5
"""

name = input("Enter your name: ")
print("Hello, World! Hello, %s!" % name)
