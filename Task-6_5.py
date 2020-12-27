"""
    Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
    и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
    Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
    что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ['красной', 'красным']

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем {Stationery.title[0]} ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем {Stationery.title[1]} карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем {Stationery.title[1]} маркером')


test = Stationery()
test.draw()

test = Pen()
test.draw()

test = Pencil()
test.draw()

test = Handle()
test.draw()
