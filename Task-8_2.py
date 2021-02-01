"""
    Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
    вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
    и не завершиться с ошибкой
"""


class MyZeroDiv(Exception):
    def __init__(self, text):
        self.txt = text


user_number1 = input('Введите делимое: ')
user_number2 = input('Введите делитель: ')
try:
    if float(user_number2) == 0:
        raise MyZeroDiv("На 0 делить нельзя!")
except MyZeroDiv as err:
    print(err)
except ValueError:
    print("Вы ввели не число")
else:
    print(f'Результа деления {float(user_number1) / float(user_number2) :.2f}')
finally:
    print('Программа завершена.')
