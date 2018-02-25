"""
Задача 6
Преобразовать массив так, чтобы сначала шли все отрицательные
элементы, а потом положительные (0 считать положительным).
Порядок следования должен быть сохранен.
"""

list_numbers = []

while True:
    try:
        num = int(input("Введите число: "))
    except ValueError:
        break

    list_numbers.append(int(num))

for i in range(len(list_numbers)):
    if list_numbers[i] >= 0:
        list_numbers.append(list_numbers[i])
        list_numbers[i] = None

while None in list_numbers:
    list_numbers.remove(None)

print(list_numbers)
