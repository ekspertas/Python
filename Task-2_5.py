# Реализовать структуру «Рейтинг»

my_list = [8, 7, 5, 3, 3]
print(f'Рейтинг натуральных чисел в порядке убывания:\n {my_list}')
user_answer = 1
while user_answer == 1:
    user_number = int(input('Введите натуральное число: '))
    if my_list.count(user_number) >= 1:
        my_list.reverse()
        my_list.insert(my_list.index(user_number), user_number)
        my_list.reverse()
    elif my_list.count(user_number) == 0 and user_number < my_list[len(my_list) - 1]:
        my_list.append(user_number)
    else:
        for el in range(len(my_list)):
            if user_number > my_list[el]:
                my_list.insert(my_list.index(my_list[el]), user_number)
                break
    print(f'Рейтинг натуральных чисел в порядке убывания:\n {my_list}')
    user_answer = int(input('Хотите продолжить? (1 - да, 0 - нет): '))
    if user_answer != 1 and user_number != 0:
        user_answer = int(input('Хотите продолжить? (1 - да, 0 - нет): '))
