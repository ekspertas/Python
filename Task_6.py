# Расчет результата спортмена

user_dist = float(input("Введите сколько киломметров пробежал спортсмен в 1-й день ?: "))
user_dist_max = float(input("Введите солько киломметров надо пробежать в день ?:"))
day_number = 1
print("Дистанция пробежки по дням:")
while user_dist <= user_dist_max:
    print(day_number, "-й день: %.2f" % user_dist, "км.")
    day_number = day_number + 1
    user_dist = user_dist * 1.1
print(day_number, "-й день: %.2f" % user_dist, "км.")
print("Спортсмен пробежит не менее %.2f" % user_dist_max, "км на ", day_number, "-й день")
