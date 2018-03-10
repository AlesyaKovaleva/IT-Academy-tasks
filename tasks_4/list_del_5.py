"""
Задача 5
Сжать список, удалив из него все 0 и заполнить
освободившиеся справа элементы значениями -1.
"""

list_numbers = []

while True:
    num = input("Enter number: ")
    if num.isnumeric() is False:
        break
    list_numbers.append(int(num))

list_numbers.sort(reverse=True)

while 0 in list_numbers:
    list_numbers.remove(0)
    list_numbers.append(-1)

print(list_numbers)
