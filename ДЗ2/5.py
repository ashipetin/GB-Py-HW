i = [7, 5, 3, 3, 2]
x = int(input("Введите новый элемент рейтинга: "))
y = len(i)
while y > 0:
    if x <= i[y-1]:
        i.insert(y,x)
        y = 0
    elif x > i[y-1] and x < i[0]:
        y = y - 1
    elif x > i[0]:
        i.insert(0,x)
        y = 0
print("Рейтинг со включенным элементом:",i)