# Проверка типа данных в списке

my_list = ['True', 'text', 65, -0.32, False, 0.8, 5+6j]
print(f"Список состоит из элементов: {my_list}")
for index in range(len(my_list)):
    print(f"Тип элемента {index} - {type(my_list[index])}")
