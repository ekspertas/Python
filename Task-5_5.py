"""
     Создать (программно) текстовый файл, записать в него программно набор чисел,
     разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("my_file.txt", 'w+') as f_1:
    digits = "32 18 -0.25 3.68 -25.4 7"
    f_1.write(digits)
    f_1.seek(0)
    digits_list = f_1.read()
    digits_list = map(float, digits_list.split())
    print(f'Сумма чисел', digits, 'равна', sum(digits_list))
