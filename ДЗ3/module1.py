def summa(ar1, ar2):
    res = ar1 + ar2
    sub = ar1 - ar2
    return res, sub
#после ретурна в том же отступе бесполезно что-то писать, не выведет
a = summa(3,5)
print(a)

c = 3
d = 5
a, b = summa(c,d)
print(a,b)

#пропуск части недописанной функции

def my_print(ar2, ar4):
    pass
print("hi")

#позиционные / обазятельные (как выше - первый по порядку равен первому итд)
#именованные:
    #def second_func(var_2,var_1,var_3):
    #second_func(var_1=10, var_2=20, var_3=30))

#Необязательные:
    #def second_func(var1, var_2=20, var_3=30):
    #print(second_func(10))

'''
Если не знаю, сколько аргументов нужно
def my_f(*args):
    return args

print(my_f(3, 4, 5, 555, 'sd'))


Неопред число именованных аргументов
def my_f2(**kwargs):
    return kwargs
print(my_f2(d = 2, h = 22, a = 'asd', l = True))

'''
def