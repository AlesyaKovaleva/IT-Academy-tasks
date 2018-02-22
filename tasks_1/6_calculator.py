"""
Написать программу “Калькулятор“, которая умеет выполнять простые
арифметические операции (сложение, вычитание, умножение, деление)
над двумя числами. Числа запрашиваются у пользователя
“Enter first operand:“, “Enter second operand:“.
Операция также запрашивается “Enter operator:” где указывается
‘+’, ‘-’, ‘/’, ‘*’. Результат вывести в виде, например, “Result: 12".
Если пользователь ввел, отличную от разрешенных, операцию результат
должен быть ‘Result: NaN’ (NaN - сокр. от Not a Number).
"""

"""
Change your code to calculate more than once. 
Make provision to exit from the program.

Algorithm: https://goo.gl/fJdGtA
"""

while True:
    print("\nCalculator\n")

    first_operand = float(input("Enter first operand: "))
    operator = input("Enter operator: ")
    second_operand = float(input("Enter second operand: "))

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

    repeat = input("\nIf you want to continue press 'y': ")
    if repeat.lower() != 'y':
        break
