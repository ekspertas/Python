# Реализовать структуру данных «Товары»

goods_list = []
count = int(input('Введите количество товаров: '))
for index in range(count):
    goods_description = []
    print(f'Товар № {index + 1}:')
    name = input('Введите наименование: ')
    price = float(input('Введите цену: '))
    quantity = int(input('Введите количество: '))
    unit = input('Введите единицу измрения: ')
    product = {'Наименование:': name, 'Цена': price, 'Количество': quantity, 'Единица измерения': unit}
    goods_description.append(index + 1)
    goods_description.append(product)
    goods_list.append(tuple(goods_description))
print(goods_list)

# Старался сделать сам. За 2 дня так и не получилось.
# надеюсь разберусь со временем .....

# test_dict = []
# test_list = []
# for index in range(count):
#     test_list = goods_list[index][1]
#     for key, val in test_list.items():
#        test_dict.append(test_list.get('Наименование:'))

# print(test_dict)
