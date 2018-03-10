# -*- coding: utf-8 -*-

"""
Задача 1
Дана целая матрица А(N,N). Составить программу подсчета среднего
арифметического значения элементов матрицы.
"""


def matrix_average(matrix):
    sum_values = 0
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            sum_values += value
            count += 1
    return sum_values/count


def main():
    matrix1 = [[10, 10, 10],
               [10, 10, 10],
               [10, 10, 10]]
    print(matrix_average(matrix1))


if __name__ == '__main__':
    main()


# OR

# from functools import reduce
#
#
# def sum_matrix(x, y):
#     return x + y
#
#
# matrix2 = reduce(sum_matrix, matrix1)
# result = reduce(sum_matrix, matrix2) / len(matrix2)
# print(result)
