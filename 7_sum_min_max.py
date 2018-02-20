"""
Написать программу поиска суммы минимального
и максимального из трех введенных чисел

Алгоритм: https://goo.gl/drCeg2
"""

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

minimal = min(a, b, c)
maximum = max(a, b, c)

if minimal == maximum:
    print("Числа равны")
else:
    sum_of_min_and_max = minimal + maximum
    print("Сумма минимального значения {} и максимального значени {} равна {}".format(minimal, maximum, sum_of_min_and_max))
