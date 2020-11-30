# Обмен значениями элементов списка

user_list = []
count = int(input('Введите длинну списка: '))
for index in range(count):
    user_list.append(input('Введите произвольный элемент списка: '))
print(f'Список состоит из элементов:\n {user_list} ')
altered_list = []
index = 0
while index in range(count):
    if index >= count - 1:
        altered_list.append(user_list[index])
        index += 1
    else:
        altered_list.append(user_list[index + 1])
        altered_list.append(user_list[index])
        index += 2
print(f'Измененный список состоит из элементов:\n {altered_list} ')
