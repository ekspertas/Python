"""
    Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
    Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа,
    а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""
from math import factorial


def fact(n):
    for i in range(n):
        yield factorial(i + 1)


number = int(input('Введите целое число для вычисления факториала: '))
counter = 1
for el in fact(number):
    print(f'Факториал ', counter, ' = ', el)
    counter += 1
