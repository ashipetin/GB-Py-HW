with open("numbers.txt","w+") as text:
    text.write(input("Введите числа, разделенные пробелами: "))
    text.seek(0)
    a = text.readline()
    b = map(int, a.split())
    print("Сумма введенных чисел:", sum(b))
