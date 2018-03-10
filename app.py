# -*- coding: utf-8 -*-

from matrix.matrix import read_matrix
from tasks_5.arithmetic_mean_1 import matrix_average
from tasks_5.main_diagonal_4 import positive_diagonal
from tasks_5.real_matrix_2 import find_elements_in_interval


tasks = {
    '1': [matrix_average, False],
    '2': [find_elements_in_interval, True],
    '3': [positive_diagonal, False],
}

while True:
    number_task = input("Задания:\n" 
                        "№ 1 - подсчет среднего арифметического значения элементов матрицы.\n"
                        "№ 2 - подсчет кол-ва элементов матрицы, удовлетворяющих условию р1<=a(i,j)<=p2.\n"
                        "№ 3 - подсчет кол-ва положительных элементов выше главной диагонали.\n"
                        "Введите номер задания: ")
    if number_task == '':
        break

    if number_task not in tasks:
        print("Такого задания не существует.")
    else:
        task_function, use_float = tasks[number_task]
        matrix = read_matrix(use_float=use_float)
        result = task_function(matrix)
        print("Результат: {}".format(result))
