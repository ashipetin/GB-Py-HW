#Решение по наитию))
'''
mylist = []
x = 1
for i in range(100,1001):
    if i % 2 == 0:
        mylist.append(i)
        x = x*i
print(x)
'''
# Решение с генератором (?) см. ниже
'''
x = 1
mylist = [i for i in range(100,1001)]
for i in mylist:
    if i % 2 == 0:
        x = x*i
print(x)
'''
# Не совсем понял, является ли первое решение соответствующим заданию
# (В задании говорится - "используя возможности генератора").
# Если не трудно, прокомментируйте - правильное ли какое-нибудь из этих решений?
# Оба работают и ответ одинаковый. Спасибо заранее

# Решение через reduce

from functools import reduce
mylist = [i if i % 2 == 0 else 1 for i in range(100,1001)]
ans = reduce(lambda x,y:x*y,mylist)
print(ans)
