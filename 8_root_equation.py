"""
Для двух чисел Х,У определить, являются ли они
корнями уравнения А*X^4+D*X^2+C=0

Алгоритм: https://goo.gl/uXPxv5
"""


def root(a, b, c, x):
    result = a * x ** 4 + b * x ** 2 + c
    return result == 0


a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

x = float(input("x = "))
y = float(input("y = "))

if root(a, b, c, x):
    print("x = {} - корень уравнения".format(x))
else:
    print("x = {} - не корень уравнения".format(x))

if root(a, b, c, y):
    print("y = {} - корень уравнения".format(y))
else:
    print("y = {} - не корень уравнения".format(y))
