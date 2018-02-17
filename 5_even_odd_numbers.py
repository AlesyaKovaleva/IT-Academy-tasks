"""
Написать программу, которая определяет четное число
или нечетное. Число запрашивается у пользователя.

Алгоритм: https://goo.gl/h52Wxr
"""

number = int(input("Enter the number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
