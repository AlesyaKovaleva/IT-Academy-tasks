"""
Задача 1
Написать программу нахождения простых чисел, используя решето Эратосфена.
Для каждой из пользовательских функций написать функцию-тест.
"""


def input_eratosfen_sieve():

    last_of_eratosfen = int(input("Для нахождения всех простых чисел\nв диапазоне от 2х до N\nВведите N: "))

    while True:
        if last_of_eratosfen < 2:
            last_of_eratosfen = int(input("Неверно задан диапазон. Введите число больше 2х: "))
        else:
            break

    return last_of_eratosfen


def eratosfen_sieve(last_number):
    eratosfen = list(range(2, last_number + 1))

    for number in eratosfen:
        if number != 0:
            for not_simple_numbers in range(2 * number, last_number + 1, number):
                eratosfen[not_simple_numbers - 2] = 0

    prime_number = list(filter(lambda x: x != 0, eratosfen))
    return prime_number


# print(eratosfen_sieve(input_eratosfen_sieve()))


def test_eratosfen_sieve_1():
    last_number = 60
    if eratosfen_sieve(last_number) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]:
        print('Test is OK')
    else:
        print('Test is NOT OK')


def test_eratosfen_sieve_2():
    last_number = 30
    if eratosfen_sieve(last_number) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        print('Test is OK')
    else:
        print('Test is NOT OK')


def test_eratosfen_sieve_3():
    last_number = 3
    if eratosfen_sieve(last_number) == [2, 3]:
        print('Test is OK')
    else:
        print('Test is NOT OK')


def test_eratosfen_sieve_4():
    last_number = 2
    if eratosfen_sieve(last_number) == [2]:
        print('Test is OK')
    else:
        print('Test is NOT OK')


test_eratosfen_sieve_1()
test_eratosfen_sieve_2()
test_eratosfen_sieve_3()
test_eratosfen_sieve_4()
