# Функция конвертации слов списка (первая буква заглавная) .

def int_func(my_str):
    if not my_str.istitle():
        return my_str.capitalize()
    return my_str


user_str = input('Введите слова разделяя их пробелом: ')
print(f'Исходный список: {user_str}')
my_list = user_str.split()
result_list = []
for el in range(len(my_list)):
    result_list.append(int_func(my_list[el]))
print(f"Преобразованный список: {' '.join(result_list)}")
