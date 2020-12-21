"""
     Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
     В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
     .......................
     Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 8}

    def running(self):
        for step in range(5):
            for key in self.__color:
                for i in reversed(range(self.__color[key])):
                    print(f'{key} горит: {i + 1}')
                    time.sleep(1)
            for x in reversed(range(self.__color['Желтый'])):
                print(f'Желтый горит: {x + 1}')
                time.sleep(1)


start = TrafficLight()
start.running()
