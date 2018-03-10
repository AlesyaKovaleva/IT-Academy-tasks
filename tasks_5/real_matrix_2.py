# -*- coding: utf-8 -*-

"""
Задача 2
Дана вещественная матрица А(3,4).
Составить программу подсчета количества элементов матрицы,
удовлетворяющих условию р1<=a(i,j)<=p2.
Значения р1 и р2 запрашиваются у пользователя.
"""


def matrix_condition():
    while True:
        try:
            first_number = float(input("Введите первое число: "))
            break
        except ValueError:
            print("Вы ввели неверное значение.")

    while True:
        try:
            second_number = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Вы ввели неверное значение.")
    return first_number, second_number


def real_matrix(matrix, p1, p2):
    """
    Функция принимает матрицу и значения р1 и р2.
    Возвращает количество чисел соответствующих
    условию р1<=a(i,j)<=p2
    """
    amount_numbers = 0

    for i in matrix:
        for j in i:
            if p1 <= j <= p2:
                amount_numbers += 1
    return amount_numbers


def find_elements_in_interval(matrix):
    a, b = matrix_condition()
    result = real_matrix(matrix, a, b)
    return result


def main():
    some_matrix = [[1.5, 2.6, 3.7, 4.8],
                   [5.9, 6.1, 7.2, 8.4],
                   [9.0, 8.8, 7.7, 6.5]]
    print(real_matrix(some_matrix, *matrix_condition()))


if __name__ == '__main__':
    main()
