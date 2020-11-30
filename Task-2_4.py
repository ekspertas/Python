# Вывод слов введенных пользователем (не более 10 символов)

user_str = input('Введите несколько слов разделяя их пробелом: ')
user_str = user_str.split()
for index in range(len(user_str)):
    print(f'{index + 1}: {user_str[index][0:10]}')
