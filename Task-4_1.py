# Реализация скрипта, в котором предусмотрена функция расчета заработной платы сотрудника.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--work_hours', type=float)
parser.add_argument('--rate_in_hour', type=float)
parser.add_argument('--bonus', type=float)
args = parser.parse_args()


def my_func(work_hours, rate_in_hour, bonus):
    return work_hours * rate_in_hour + bonus


print(f'Зарплата сотрудника: {my_func(args.work_hours, args.rate_in_hour, args.bonus):.2f}')
# Запуск из командной строки (пример): python Task-4_1.py --work_hours=10 --rate_in_hour=7 --bonus=120
