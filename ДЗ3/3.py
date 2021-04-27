def my_func(ar1,ar2,ar3):
    x = max(ar1,ar2) + max(ar2,ar3)
    return x
a = my_func(
int(input("Введите аргумент 1: ")),
int(input("Введите аргумент 2: ")),
int(input("Введите аргумент 3: "))
)
print("Сумма наибольших аргументов =",a)
