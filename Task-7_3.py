"""
    Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов:
    и т.д.
"""


class Cell:
    def __init__(self, unit):
        self.unit = unit

    def __add__(self, other):
        return f'Число ячеек общей клетки:  {self.unit + other.unit}'

    def __sub__(self, other):
        if (self.unit - other.unit) >= 0:
            return f'Общая клетка состоит из  {self.unit - other.unit} ячеек(ки)'
        else:
            return f'Разница ячеек в клетках отрицательное число'

    def __mul__(self, other):
        return f'Общая клетка состоит из  {self.unit * other.unit} ячеек(ки)'

    def __truediv__(self, other):
        return f'Общая клетка состоит из  {self.unit // other.unit} ячеек(ки)'

    def make_order(self, row):
        row_count = self.unit // row
        new_format = str()
        for i in range(row_count):
            for j in range(row):
                new_format = new_format + '*'
            new_format = new_format + '/n'
        if self.unit % row > 0:
            for i in range(self.unit % row):
                new_format = new_format + '*'
        else:
            new_format = new_format[:-1]
            new_format = new_format[:-1]
        return new_format


cell_1 = Cell(35)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
