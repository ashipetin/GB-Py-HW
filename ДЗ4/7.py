def fact(n):
    x = 1
    for i in range(2,n+1):
        x *= i
    yield x
n = int(input("Введите число для нахождения его факториала: "))
for el in fact(n):
    print(f"Факториал числа {n}:",el)