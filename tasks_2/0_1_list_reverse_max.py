"""
Задача 0
   Дан список А1..AN. Вывести элементы списка в обратном порядке.
"""

list_number = [1, 2, 3, 4, 5, 6]
list_number.reverse()
print(list_number)


"""
Задача 1
   Исключить из списка А1..AN максимальный элемент.
"""

list_number.remove(max(list_number))
print(list_number)
