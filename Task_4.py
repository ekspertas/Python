# Поиск наибольшей цифры в числе

user_Num = int(input("Введите целое положительное число: "))
user_Num_Info = user_Num
max_Num = 0
while user_Num % 10 > 0:
    n = (user_Num % 10)
    user_Num = user_Num // 10
    if max_Num < n:
        max_Num = n
print("Максимальнаой цифрой в числе", user_Num_Info, "является ", max_Num)
