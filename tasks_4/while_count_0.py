"""
Задача 0
Написать программу, которая предлагает пользователю ввести список чисел,
после чего  запрашивает число для которого нужно посчитать сколько раз
оно встречается в списке.
"""

list_numbers = []
counter = 0

while True:
    num = input("Enter number: ")
    if not num.isnumeric():
        break
    list_numbers.append(int(num))

number = int(input("Enter number to count: "))

for num in list_numbers:
    if num == number:
        counter += 1

print("The number '{}' repeated '{}' times".format(number, counter))
