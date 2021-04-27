def my_func(**kwargs):
    return kwargs
x = 1
total = 0
while x > 0:
    a = input("Введите числа, разделенные пробелами. Стоп-символ: 's'; ")
    b = a.split(sep = " ")
    if "s" in b:
        for element in range(0, b.index("s")):
                total = total + int(b[element])
        x = 0
        print("Вы ввели стоп-символ. Сумма всех чисел до него:", total)
    else:
        for element in range(0, len(b)):
            total = total + int(b[element])
    print(total)
