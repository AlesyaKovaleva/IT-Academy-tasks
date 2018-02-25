"""
Задача 1
Определить, является ли введенное слово идентификатором, т.е.
начинается ли оно с английской буквы в любом регистре или
знака подчеркивания и не содержит других символов, кроме букв
английского алфавита (в любом регистре), цифр и знака подчеркивания.
"""

word = input("Enter your identifier: ").lower()

identifier = list(word)

if identifier[0] == "_" or "a" <= identifier[0] <= "z":
    for i in range(1, len(identifier)):
        if not(identifier[i] == "_" or "a" <= identifier[i] <= "z" or "0" <= identifier[i] <= "9"):
            print("It's not identifier!")
    print("It's identifier!")
else:
    print("It's not identifier!")

# OR

word = input("Enter your identifier: ").lower()

if word.isidentifier():
    print("It's identifier!")
else:
    print("It's not identifier!")
