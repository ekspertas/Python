"""
    Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
    «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
    Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
    должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_conversion(cls, input_str):
        input_str = input_str.replace('-', ' ')
        date_list = list(map(int, input_str.split(' ')))
        return date_list

    @staticmethod
    def validation(int_list):
        check = False
        if not 1 <= int_list[0] <= 31:
            print(f'День должен находиться в пределах от 1 до 31')
        else:
            if not 1 <= int_list[1] <= 12:
                print(f'Месяц должен находиться в пределах от 1 до 12')
            else:
                if not 1 <= int_list[2] <= 9999:
                    print(f'Год должен находиться в пределах от 1 до 9999')
                else:
                    print(f'Корректный формат даты:')
                    print(' '.join(str(item) for item in int_list))
                    check = True
        return check


user_check = False
while not user_check:
    user_date = input('Введите число, месяц и год в формате день-месяц-год: ')
    user_check = Date.validation(Date.date_conversion(user_date))
