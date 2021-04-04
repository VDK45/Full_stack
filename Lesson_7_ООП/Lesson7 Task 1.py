"""
    1. Реализовать класс Matrix (матрица). 
    Обеспечить перегрузку конструктора класса (метод __init__()), 
    который должен принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — система некоторых математических величин, 
    расположенных в виде прямоугольной схемы.
    Примеры матриц вы найдете в методичке.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__() 
    для реализации операции сложения двух объектов класса Matrix (двух матриц). 
    Результатом сложения должна быть новая матрица.
    Подсказка: сложение элементов матриц выполнять поэлементно — 
    первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

a = [[1, 2, 3, 4], [5, 5, 5, 5], [6, 7, 8 ,9]]
b = [[9, 8, 7, 6], [5, 5, 5, 5], [4, 3, 2, 1]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists
        
    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))

matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 12}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 12}")
print(f"Matrix 1 + Matrix 2\n{matrix_1 + matrix_2}")

print('---------------- Вариант ---------------------')

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        new_m = []
        for i in range(len(self.matrix)):
            new_m.append([])
            for d in range(len(self.matrix[i])):
                new_m[i].append(self.matrix[i][d] + other.matrix[i][d])
        return Matrix(new_m)

    def __str__(self):
        new_m = []
        for i in range(len(self.matrix)):
            for d in range(len(self.matrix[i])):
                new_m.append(f"{self.matrix[i][d]}\t")
            new_m.append("\n")
        return f'{"".join(new_m)}'


a = Matrix([[1, 2], [3, 4], [5, 6]])
print(f"{a}{'-' * 9}")
b = Matrix([[8, 7], [6, 5], [4, 3]])
print(f"{b}{'-' * 9}")
print(a + b)

print('---------------- Вариант ---------------------')

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([str(itm) for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:

            return f"Ощибка размерностей матриц"

m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_2 = [['9', '8', '7'], ['6', '5', '4'], ['3', '2', '1']]
mt1 = Matrix(m_1)
mt2 = Matrix(m_2)
print('------mt1--------')
print(mt1)
print('------mt2--------')
print(mt2)
print('----mt1 + mt2----')
print(mt1 + mt2)

m_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_4 = [['9', '8', '7'], ['6', '5', '4'], ['3', '2']] 
mt3 = Matrix(m_3)
mt4 = Matrix(m_4)
print('------mt3--------')
print(mt3)
print('------mt4--------')
print(mt4)
print('----mt3 + mt4----')
print(mt3 + mt4)

print('---------------- Вариант ---------------------')

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '  '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))

my_m1 = Matrix([[1, 2], [3, 4], [5, 6]])
my_m2 = Matrix([[8, 7], [6, 5], [4, 3]])
print(my_m1)
print(my_m2)
s = my_m1 + my_m2

print(s)

print('---------------- Вариант ---------------------')

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        return Matrix([map(sum, zip(*t)) for t in zip(self.matrix, other.matrix)])

stroki = int(input('Введите количество строк и стобцов матриц: '))
stolbci = stroki

matrix1 = Matrix([[i * j for j in range(stroki)] for i in range(stolbci)])
matrix2 = Matrix([[i + j for j in range(stroki)] for i in range(stolbci)])

print('First matrix:\n', matrix1, end='\n\n')
print('Second matrix:\n', matrix2, end='\n\n')
print('Сума двух матриц:\n', matrix1 + matrix2 )
