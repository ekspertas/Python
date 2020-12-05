# Функция суммы наибольших двух чисел

def my_func(arg_1, arg_2, arg_3):
    if arg_1 <= arg_2 and arg_1 <= arg_3:
        return arg_2 + arg_3
    elif arg_2 <= arg_1 and arg_2 <= arg_3:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2


print(f'Вычисление суммы наибольших двух чисел')
user_arg_1 = float(input('Введидете первое число: '))
user_arg_2 = float(input('Введите второе число: '))
user_arg_3 = float(input('Введите третье число: '))
print(f'Результат {my_func(user_arg_1, user_arg_2, user_arg_3):.2f}')
