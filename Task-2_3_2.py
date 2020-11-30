# Определение времени года используя словарь

seasons_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень'}
month_num = int(input('Введите порядковый номер мясяца в году (1-12): '))
dict_key = ((month_num + 12) // 3) - 4
if month_num == 12:
    print(f'Время года: {seasons_dict[0]}')
else:
    print(f'Время года: {seasons_dict[dict_key]}')
