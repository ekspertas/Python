# Определение времени года используя список
# формулу рассчета индекса списка "вымучал" сам

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
month_num = int(input('Введите порядковый номер мясяца в году (1-12): '))
index = ((month_num + 12) // 3) - 4
if month_num == 12:
    print(f'Время года: {seasons_list[0]}')
else:
    print(f'Время года: {seasons_list[index]}')
