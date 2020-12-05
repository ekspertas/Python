# Функция деления чисел

def my_division(arg_1, arg_2):
    return float(arg_1 / arg_2)


user_arg_2 = 0
while user_arg_2 == 0:
    user_arg_1 = float(input('Введите делимое: '))
    user_arg_2 = float(input('Введите делитель: '))
    if user_arg_2 != 0:
        print(f'Результат деления {my_division(user_arg_1, user_arg_2):.2f}')
    else:
        print(f'Деление на "0" невозможно:')
