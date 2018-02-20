"""
Если среди трех чисел А,В,С имеется хотя бы одно
четное вычислить максимальное, иначе - минимальное

Алгоритм: https://goo.gl/gQLPHu
"""

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

if a == b == c:
    print("Числа равны")
elif a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    maximum = max(a, b, c)
    print("Максимальное значение: {}".format(maximum))
else:
    minimal = min(a, b, c)
    print("Минимальное значение: {}".format(minimal))
