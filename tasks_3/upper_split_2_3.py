"""
Задача 2
   Дана строка ‘Hello!Anthony!Have!A!Good!Day!’.
   Создать список, состоящий из отдельных слов
   [‘HELLO’, ‘ANTHONY’, ‘HAVE’, ‘A’, ‘GOOD’, ‘DAY’].
"""

string = 'Hello!Anthony!Have!A!Good!Day!'

string = string.upper().split('!')
string = string if string[-1] != '' else string[:-1]
string.sort()


"""
* Задача 3
   Полученный список из задачи 2 вывести столбиком 
   в отсортированном порядке.
"""

print('\n'.join(string))
