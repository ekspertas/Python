"""
     Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
     лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
     предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
     количество занятий по нему. Вывести словарь на экран
"""

with open("my_file.txt") as f_1:
    profit = 0
    counter = 0
    all_profits = 0
    firms_names = []
    firms_profit = []
    for line in f_1:
        counter += 1
        temp_list = line.split()
        firms_names.append(temp_list[0])
        profit = float(temp_list[2]) - float(temp_list[3])
        firms_profit.append(profit)
        if profit >= 0:
            all_profits = float(all_profits) + profit
        else:
            counter -= 1
    firms_dict = {firms_names[i]: firms_profit[i] for i in range(len(firms_names))}
    avg_profit_dict = {'average_profit': round(float(all_profits / counter), 2)}
    final_list = [firms_dict, avg_profit_dict]
    print(final_list)
import json
with open("my_file.json", "w") as write_f:
    json.dump(final_list, write_f)
    json_str = json.dumps(final_list)
    print(json_str)
