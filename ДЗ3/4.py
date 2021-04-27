# Возведение в степень (**)
'''
def my_func(x,y):
    ans = x**y
    return ans
a = my_func(
float(input("Введите действительное положительное число: ")),
int(input("Введите целое отрицательное число: ")))
print(a)
'''
# С помощью цикла
def my_func(x,y):
    d = -1
    ans = 1/x
    while d > y:
        ans = ans*(1/x)
        d -= 1
    return ans
a = my_func(
float(input("Введите действительное положительное число: ")),
int(input("Введите целое отрицательное число: ")))
print(a)
