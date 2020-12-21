"""
     Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
     income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
     премия, например, {"wage": wage, "bonus": bonus}.
     И т. д. .....
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self. name = name
        self. surname = surname
        self. position = position
        self. _income = {"Оклад": wage, "Премия": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник фирмы: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход сотрудника {self.position}',
              round(self._income['Оклад'] + self._income['Премия'], 2), 'руб')


workers_number = int(input('Сколько человек работают в фирме?: '))
for i in range(workers_number):
    user_name = input('Введите имя сотрудника: ')
    user_surname = input('Введите фамилию сотрудника: ')
    user_position = input('Введите должность сотрудника: ')
    user_wage = float(input('Введите оклад сотрудника: '))
    user_bonus = float(input('Введите премию сотрудника: '))
    firm_worker = Position(user_name, user_surname, user_position, user_wage, user_bonus)
    print(f'Значения атрибутов класса: {firm_worker.name} {firm_worker.surname} {firm_worker.position}'
          f' {firm_worker._income} ')
    firm_worker.get_full_name()
    firm_worker.get_total_income()
