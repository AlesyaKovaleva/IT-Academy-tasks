"""
На вход поступают две строки. Необходимо выяснить,
является ли вторая строка подстрокой первой.
"""

string = input("Введите строку: ")
substring = input("Введите подстроку: ")

if substring.lower() in string.lower():
    print('Подстрока "{}" входит в строку "{}"'.format(substring, string))
else:
    print('Подстрока "{}" не входит в строку "{}"'.format(substring, string))
