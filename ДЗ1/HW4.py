earn = float(input("Введите выручку: "))
cost = float(input("Введите издержки: "))
if earn > cost:
    print("Вы в прибыли")
    print("Рентабельность выручки:", (earn-cost)/earn)
    hc = int(input("Введите численность сотрудников:"))
    print("Прибыль на одного сотрудника:", (earn-cost)/hc)
elif earn == cost: print("Выручка равна издержкам")
else: print("Вы в убытке")
