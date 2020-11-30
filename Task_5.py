# Вычисление результатов работы фирмы

firm_Receipts = float(input("Введите сумму выручки фирмы: "))
firm_Expenses = float(input("Введите сумму издержек (затрат) фирмы: "))
firm_Result = firm_Receipts - firm_Expenses
if firm_Result >= 0:
    print("Фирма заработала прибыль в размере: %.2f" % firm_Result, "руб."
          "\nРентабельность выручки: %.2f" % (firm_Result / firm_Receipts))
    firm_Employees = int(input("Сколько сотрудников работает в фирме ?: "))
    print("Прибыль фирмы в расчете на одного сотрудника: %.2f" % (firm_Result / firm_Employees), "руб.")
else:
    print("Фирма работала с убытком в размере: %.2f" % firm_Result, "руб.")
