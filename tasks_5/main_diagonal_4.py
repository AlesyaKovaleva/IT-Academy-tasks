# -*- coding: utf-8 -*-

"""
Задача 4*
Дана квадратная матрица А(N,N).
Составить программу подсчета количества положительных элементов,
расположенных выше главной диагонали.
"""


def positive_diagonal(matrix):
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            value = matrix[i][j]
            if i < j and value > 0:
                count += 1
    return count


def main():
    matrix1 = [[1, 5, -4, -6, 7],
               [-5, 1, 5, -8, 3],
               [6, 3, 1, -3, -5],
               [-6, 6, 0, 1, 12],
               [5, 0, -3, 5, 1]]
    print(positive_diagonal(matrix1))


if __name__ == '__main__':
    main()
