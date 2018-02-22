"""
Ввести три числа А,В,С. Удвоить каждое из них,
если А>=В>=С, иначе поменять значения А и В.

Алгоритм: https://goo.gl/2FZKQf
"""

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

if a >= b >= c:
    a *= 2
    b *= 2
    c *= 2
else:
    a, b = b, a

print("A = {}, B = {}, C = {}".format(a, b, c))
