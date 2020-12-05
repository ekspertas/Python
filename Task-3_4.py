# Функция возведение числа x в степень y.

def my_func(x, y):
    return x**y


def my_func_loop(x, y):
    result = 1
    counter = 1
    while counter <= abs(y):
        result = result * x
        counter += 1
    return 1 / result


user_num1 = float(input('Введите положительное число: '))
user_num2 = int(input('Введите отрицательное целое число: '))
print(f'Результат возведения числа ', user_num1, ' в степень ', user_num2)
print(f'Первый способ: {my_func(user_num1, user_num2):.6f}')
print(f'Второй способ: {my_func_loop(user_num1, user_num2):.6f}')
