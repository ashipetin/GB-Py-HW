a = int(input("Километров в первый день?"))
b = int(input("Цель спортсмена?"))
day = 1
while a < b:
    a = a * 1.1
    day = day + 1
print(f"Ответ: на {day}-й день спортсмен достиг результата - не менее {b} км.")
