ar1 = int(input("Введите первый аргумент: "))
ar2 = int(input("Введите второй аргумент: "))
def division(ar1,ar2):
    if ar2 == 0:
        return "Error: division by zero"
    else:
        res = ar1 / ar2
    return res
print(division(ar1,ar2))