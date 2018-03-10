"""
Задача 0
Дан список А1..AN. Найти элемент, который чаще всего встречается,
вывести его значение и количество повторений.
"""


def input_elements():
    list_elements = []

    while True:
        element = input("Enter value: ")
        if element == "":
            break
        list_elements.append(element)
    return list_elements


def reiteration(some_list):
    dict_elements = {}

    for element in some_list:
        if element in dict_elements:
            dict_elements[element] += 1
        else:
            dict_elements[element] = 1
    return "The most common element: '{}' is repeated {} times".format(*max(dict_elements.items(), key=lambda x: x[1]))


print(reiteration(input_elements()))
