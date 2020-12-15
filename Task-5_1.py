"""
    Создать программно файл в текстовом формате, записать в него построчно данные,
    вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open("text.txt", 'w') as f_1:
    user_str = (input('Введите данные для заниси и нажмите "Enter" (для выхода нажмите "Enter"): '))
    f_1.write(user_str + '\n')
    while user_str:
        user_str = (input('Введите данные для заниси и нажмите "Enter" (для выхода нажмите "Enter"): '))
        f_1.write(user_str + '\n')
with open("text.txt") as f_1:
    text = f_1.read()
    print(text)
