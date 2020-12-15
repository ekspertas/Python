"""
    Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("my_file.txt") as f_1:
    counter = 0
    for line in f_1:
        counter += 1
        print(f'Строка файла: {line.strip()}')
        temp_list = line.split()
        print(f'Количество слов в строке: {len(temp_list)}')
    print(f'\nКоличество строк в файле: {counter}')
