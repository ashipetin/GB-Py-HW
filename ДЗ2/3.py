season = {"Весна": [3,4,5], "Лето": [6,7,8], "Осень": [9,10,11], "Зима": [12,1,2]}
while True:
    try:
        mon = int(input(("Введите номер месяца: ")))
        if mon < 1 or mon > 12:
            print("Такого месяца нет. Попробуйте снова")
            continue
    except ValueError:
        print("Введите только число от 1 до 12")
        continue
    else:
        break
if mon in season["Весна"]:
    print("Ваш сезон: Весна")
elif mon in season["Лето"]:
    print("Ваш сезон: Лето")
elif mon in season["Осень"]:
    print("Ваш сезон: Осень")
elif mon in season["Зима"]:
    print("Ваш сезон: Зима")
