"""
    Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее
"""
from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

counter = 0
my_list = ["Петя", "Вася", "Федя"]
for el in cycle(my_list):
    if counter > 10:
        break
    print(el)
    counter += 1
