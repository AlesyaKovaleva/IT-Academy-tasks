# -*- coding: utf-8 -*-


def read_matrix(use_float=False):
    """
    Функция формирует и возвращает матрицу заданного размера.
    Размер и значения запрашиваются у пользователя.
    """
    while True:
        try:
            line = int(input("Введите количество строк в матрице: "))
            if line <= 0:
                raise ValueError
            break
        except ValueError:
            print("Вы ввели неправильное значение.")

    while True:
        try:
            column = int(input("Введите количество столбцов в матрице: "))
            if column <= 0:
                raise ValueError
            break
        except ValueError:
            print("Вы ввели неправильное значение.")

    matrix = []

    for i in range(column):
        matrix.insert(i, [])
        for j in range(line):
            while True:
                try:
                    if use_float:
                        value = float(input("Введите A[{}][{}]:".format(i, j)))
                    else:
                        value = int(input("Введите A[{}][{}]:".format(i, j)))
                    break
                except ValueError:
                    print("Вы ввели неправильное значение.")

            matrix[i].insert(j, value)

    print("Ваша матрица:")
    for row in matrix:
        print(row)

    return matrix
