"""
Задача 2
Найти и вывести все гласные буквы (без повторений), которые встречаются
в самом коротком слове. Текст запрашивается у пользователя.
Алфавит использовать любой.
"""

text = input("Enter your text: ").lower()

min_length = len(text)
words = text.split()
word = words[0]

for i in words:

    if len(i) < min_length:
        min_length = len(i)
        word = i


VOWELS_ENG = ['a', 'e', 'i', 'o', 'y', 'u']
VOWELS_RUS = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
VOWELS = VOWELS_ENG + VOWELS_RUS

found_vowels = set()

for i in word:
    if i in VOWELS:
        found_vowels.add(i)

print('Гласные буквы в самом коротком слове: "{}" это: {}'.format(word, ', '.join(found_vowels)))
