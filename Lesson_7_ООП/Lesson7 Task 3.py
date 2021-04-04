"""
    3. Реализовать программу работы с органическими клетками. 
    Необходимо создать класс Клетка. 
    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
    В классе должны быть реализованы методы перегрузки арифметических операторов: 
    сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам и выполнять 
    увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. 
    В методе деления должно осуществляться округление значения до целого числа.
    Сложение. Объединение двух клеток. 
    При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    Вычитание. Участвуют две клетки. 
    Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе 
    выводить соответствующее сообщение.
    Умножение. Создается общая клетка из двух. 
    Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
    Деление. Создается общая клетка из двух. 
    Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
    В классе необходимо реализовать метод make_order(), 
    принимающий экземпляр класса и количество ячеек в ряду. 
    Данный метод позволяет организовать ячейки по рядам.
    Метод должен возвращать строку вида *****\n*****\n*****..., 
    где количество ячеек между \n равно переданному аргументу. 
    Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
    Тогда метод make_order() вернет строку: *****\n*****\n**.
    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
    Тогда метод make_order() вернет строку: *****\n*****\n*****.
    Подсказка: подробный список операторов для перегрузки доступен по ссылке.
    https://pythonworld.ru/osnovy/peregruzka-operatorov.html
"""

class Cell:
    def __init__(self, rows):
        self.rows = rows
        
    def __add__(self, other):
        print('Результат брибавления:')
        return Cell(self.rows + other.rows)
        
    def __sub__(self, other):
        print('Результат отнимания:')
        return Cell(abs(self.rows - other.rows))
        
    def __mul__(self, other):
        print('Результат умножения:')
        return Cell(self.rows * other.rows)
    
    def __truediv__(self, other):
        print('Результат деления:')
        return Cell(self.rows // other.rows)
    
    def __str__(self):
        return f"{self.rows}"
        
    def make_order(self, x):
        a = self.rows // x
        b = self.rows % x
        c = f"{x * '*'}\n"
        print(f"В строке по {x} звезд максимум: ")
        return print(f"{c * a}{b * '*'}")
        
a1 = Cell(333)
a2 = Cell(3)
print(a1 + a2 + a1 )
print(a1 * a2 * a1 )
print(a1 - a2 - a2)
try:
    print(a1 / a2 / a2)
except ZeroDivisionError as err:
    print("Zero Division Error")

(a1 / a2 / a2).make_order(9)

print('------------------ Учительская 1 -------------------')

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print('Sum of cell is: ')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Subtraction of cell is: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
               else 'Результат в минусе '
               
    def __mul__(self, other):
        print('Multiply of cell is: ')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Truediv of cell is: ')
        return Cell(self.nums // other.nums)

cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_2 // cell_1)
print(cell_1.make_order(6))
