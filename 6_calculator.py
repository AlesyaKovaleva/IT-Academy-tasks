"""
Написать программу “Калькулятор“, которая умеет выполнять простые
арифметические операции (сложение, вычитание, умножение, деление)
над двумя числами. Числа запрашиваются у пользователя
“Enter first operand:“, “Enter second operand:“.
Операция также запрашивается “Enter operator:” где указывается
‘+’, ‘-’, ‘/’, ‘*’. Результат вывести в виде, например, “Result: 12".
Если пользователь ввел, отличную от разрешенных, операцию результат
должен быть ‘Result: NaN’ (NaN - сокр. от Not a Number).

Алгоритм: https://goo.gl/fJdGtA
"""

first_operand = float(input("Enter first operand: "))
second_operand = float(input("Enter second operand: "))
operator = input("Enter operator: ")

result = None

if operator == '+':
    result = first_operand + second_operand
elif operator == '-':
    result = first_operand - second_operand
elif operator == '*':
    result = first_operand * second_operand
elif operator == '/':
    result = first_operand / second_operand
else:
    print("Result:", result)
if result is not None:
    print("Result:", result)
