"""
Написать программу, высчитывающую площадь круга.
Необходимые параметры запрашиваются у пользователя.

Алгоритм: https://goo.gl/BX2XDM
"""

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is: %.2f" % area)


# print("The area of the circle is: %.2f" % (math.pi * radius ** 2))
