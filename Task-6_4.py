"""
     Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
     is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
     остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
     И т.д.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала')

    def stop(self):
        print(f'Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля ',  self.speed, ' км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость!')
        else:
            print(f'Скорость автомобиля ', self.speed, ' км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость!')
        else:
            print(f'Скорость автомобиля ', self.speed, ' км/ч')


class PoliceCar(Car):
    def information(self):
        if self.is_police:
            print(f'Это полицейская машина!')


my_car_1 = TownCar(70, "красный", "Шевролет")
print(f'{my_car_1.color} {my_car_1.name}')
my_car_1.go()
my_car_1.show_speed()
my_car_1.turn('право')
my_car_1.stop()

my_car_2 = SportCar(110, "синий", "Плимут")
print(f'{my_car_2.color} {my_car_2.name}')
my_car_2.show_speed()
my_car_2.turn('лево')

my_car_3 = WorkCar(30, "желтый", "Камаз")
print(f'{my_car_3.color} {my_car_3.name}')
my_car_3.go()
my_car_3.show_speed()
my_car_3.turn('право')
my_car_3.stop()

my_car_4 = PoliceCar(180, "черная", "Волга", True)
print(f'{my_car_4.color} {my_car_4.name}')
my_car_4.go()
my_car_4.show_speed()
my_car_4.turn('лево')
my_car_4.information()
my_car_4.stop()


