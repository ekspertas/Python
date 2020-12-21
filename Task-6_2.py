"""
     Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
     Значения данных атрибутов должны передаваться при создании экземпляра класса.
     Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
     длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
     толщины полотна. Проверить работу метода.
"""


class Road:
    m2_wight = 25
    road_thickness = 5

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def coating_weight(self):
        return self._length * self._width * Road.m2_wight * Road.road_thickness


user_length = input('Введите длинну дороги (м): ')
user_width = input('Введите ширину дороги (м): ')
weight = Road(user_length, user_width)
print(f'Масса асфальта для покрытия: {weight.coating_weight() / 1000 :.2f} тонн')
