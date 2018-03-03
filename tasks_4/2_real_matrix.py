"""
Задача 2
Дана вещественная матрица А(3,4).
Составить программу подсчета количества элементов матрицы,
удовлетворяющих условию р1<=a(i,j)<=p2.
Значения р1 и р2 запрашиваются у пользователя.
"""

some_matrix = [[1.5, 2.6, 3.7, 4.8],
               [5.9, 6.1, 7.2, 8.4],
               [9.0, 8.8, 7.7, 6.5]]

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))


def real_matrix(matrix, p1, p2):
    amount_numbers = 0

    for i in matrix:
        for j in i:
            if p1 <= j <= p2:
                amount_numbers += 1
    return amount_numbers


print(real_matrix(some_matrix, first_number, second_number))
