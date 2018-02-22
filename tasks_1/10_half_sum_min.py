"""
Ввести два числа. Меньшее заменить их полусуммой,
а большее - удвоенным произведением.

Алгоритм: https://goo.gl/XjDvu3
"""

a = float(input("A = "))
b = float(input("B = "))

if a > b:
    a, b = (a * b * 2, (a + b) / 2)
    print(a, b)
elif b > a:
    a, b = ((a + b) / 2, a * b * 2)
    print(a, b)
else:
    print("Числа равны")
