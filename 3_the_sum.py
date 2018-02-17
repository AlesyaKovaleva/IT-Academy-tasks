"""
Написать программу, которая запрашивает у пользователя два 
целочисленных числа, и выводит результат вида “The sum of 1 and 3 is 4”.

Алгоритм: goo.gl/wcvMvj
"""

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
result = first_number + second_number
print("The sum of %d and %d is %d." % (first_number, second_number, result))

# print("The sum of {} and {} is {}.".format(first_number, second_number, result))
