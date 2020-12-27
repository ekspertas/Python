"""
Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 (отдельные строки)
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл
"""

with open("my_file.txt") as f_eng, open("output_file.txt", "w+") as f_rus:
    digits_dict = {'One': "Один", 'Two': "Два", 'Three': "Три", 'Four': "Четыре"}
    for line in f_eng:
        test_list = line.split()
        test_list[0] = digits_dict.get(test_list[0])
        f_rus.write(' '.join(test_list) + '\n')
with open("output_file.txt") as f_rus:
    text = f_rus.read()
    print(text)
