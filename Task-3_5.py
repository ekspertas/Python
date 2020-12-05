# Функция вычисления суммы чисел введенных пользователем.

def my_func(my_str):
    my_str = my_str.replace('*', '0')
    my_list = my_str.split()
    numbers = []
    for el in range(len(my_list)):
        if not my_list[el].isalpha():
            numbers.append(float(my_list[el]))
    return sum(numbers)


my_sum = 0
user_str = str()
while not user_str.endswith('*'):
    user_str = (input('Введите числа разделяя их пробелом и нажмите "Enter" (для выхода введите *): '))
    my_sum = my_sum + my_func(user_str)
    print(f'Сумма введенных чисел равна:  {my_sum:.2f}')
