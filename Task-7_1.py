"""
    Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
    который должен принимать данные (список списков) для формирования матрицы.
    и т.д.
"""

import numpy as np


class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return '\n'.join(str(item) for item in self.my_matrix)

    def __add__(self, other):
        return Matrix(self.my_matrix + other.my_matrix)


a = np.array([[2, 6, 7], [4, 8, 2]])
b = np.array([[-6, 8, 7], [5, -9, 1]])

matrix_1 = Matrix(a)
print('Объект Nr. 1 класса Matrix:')
print(matrix_1)
matrix_2 = Matrix(b)
print('Объект Nr. 2 класса Matrix:')
print(matrix_2)
print('Сумма объектов класса Matrix:')
print(matrix_1 + matrix_2)
