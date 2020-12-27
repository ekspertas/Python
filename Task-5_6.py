"""
    Создать (не программно) текстовый файл.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
    со средней прибылью. Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""

with open("my_file.txt") as f_1:
    sum_time = 0
    class_names = []
    class_times = []
    line = f_1.readline()
    while line:
        digits_list = line.split()
        class_names.append(digits_list[0])
        for el in range(len(digits_list)):
            tmp_val = digits_list[el].strip('()лпраб.')
            if tmp_val.isdigit():
                sum_time = sum_time + int(tmp_val)
        class_times.append(sum_time)
        sum_time = 0
        line = f_1.readline()
    my_dict = {class_names[i]: class_times[i] for i in range(len(class_names))}
    print(my_dict)
