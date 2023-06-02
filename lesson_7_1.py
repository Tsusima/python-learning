# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += '  '.join([str(elem) for elem in row]) + '\n'
        return result

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return 'Matrices should have same dimensions'
        else:
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)
            return Matrix(result)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 92, 15]])
m2 = Matrix([[7, 8, 9], [10, 11, 12], [0, 1, -15]])
m3 = m1 + m2
print(f"matrix 1: \n{m1} \nmatrix 2: \n{m2} \nResult of addition: \n{m3}")

