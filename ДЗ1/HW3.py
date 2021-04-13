n = int(input("Введите целое положительное число"))
x = 0
while n > 0:
    a = n % 10
    if a > x: x = a
    n = n // 10
print(x)
