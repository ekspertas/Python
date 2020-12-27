"""
     Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
     Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
     Выполнить подсчет средней величины дохода сотрудников
"""

with open("my_file.txt") as f_1:
    salary = 0
    counter = 0
    for line in f_1:
        counter += 1
        temp_list = line.split()
        salary = salary + float(temp_list[1])
        if float(temp_list[1]) < 20000:
            print(f'Фамилия сотрудника с окладом менее 20 000 руб.: {temp_list[0]}')
    print(f'\nСредний оклад сотрудников: {salary / counter :.2f} руб.')
