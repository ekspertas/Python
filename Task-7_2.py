"""
    Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
    размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
    и т.д.
"""

from abc import ABC, abstractmethod


class Clothes:
    @abstractmethod
    def __init__(self, title, parameter):
        self.title = title
        self.parameter = parameter


class Coat(Clothes):
    def __init__(self, title, v):
        self.title = title
        self.v = v

    @property
    def coat_method(self):
        return self.v/6.5 + 0.5


class Costume(Clothes):
    def __init__(self, title, h):
        self.title = title
        self.h = h

    @property
    def costume_method(self):
        return 2*self.h + 0.3


my_coat = Coat('Палантин', 48)
my_costume = Costume('Тройка', 52)
print(f'Для изготовления польта {my_coat.title} и костюма {my_costume.title}'
      f' потребуется {my_coat.coat_method + my_costume.costume_method :.2f}  квадратных метров ткани')



