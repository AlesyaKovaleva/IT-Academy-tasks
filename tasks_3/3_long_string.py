"""
Задача 3
Вводятся строки. Определить самую длинную строку и вывести ее
номер на экран. Если самая длинная строка повторяется несколько
раз, то вывести номера всех таких строк.
"""

list_text = []
max_length = 0
max_string = ''
num_index = []

while True:
    text_string = input("Введите строку: ")
    if text_string == '':
        break
    list_text.append(text_string)

for string in list_text:
    if len(string) > max_length:
        max_length = len(string)
        max_string = string

for index in range(len(list_text)):
    if list_text[index] == max_string:
        num_index.append(str(index + 1))

print("Самая длинная введённая строка № {}.".format(", ".join(num_index)))
