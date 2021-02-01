"""
    Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
    который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
    уникальные для каждого типа оргтехники.

"""


from abc import ABC, abstractmethod


class Warehouse:
    counter = 0

    def __init__(self, department, equipment):
        self.department = department
        self.equipment = equipment
        Warehouse.counter += 1

    def return_shop_list(self):
        return self.equipment


class OfficeEquipment:
    @abstractmethod
    def __init__(self, name, count, price):
        self.name = name
        self.count = int(count)
        self.price = float(price)


class Printer(OfficeEquipment):
    def __init__(self, name, count, price, laser):
        super().__init__(name, count, price)
        self.laser = bool(laser)


class Scanner(OfficeEquipment):
    def __init__(self, name, count, price, desk_top):
        super().__init__(name, count, price)
        self.desk_top = bool(desk_top)


class Copier(OfficeEquipment):
    def __init__(self, name, count, price, colored):
        super().__init__(name, count, price)
        self.colored = bool(colored)


printer = Printer('HP', 2, 33.3, True)
pos1 = Warehouse('Vilnius', printer)
print(pos1.return_shop_list())
print(printer.laser)
