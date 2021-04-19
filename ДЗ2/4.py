i = input("Введите вашу строку: слова, разделенные пробелами: ")
i = i.split(" ")
x = len(i)
y = 0
while y < x:
    if len(i[y]) > 10:
        print(y+1,". ",(i[y])[0:10],sep='')
        y += 1
    else:
        print(y+1,". ",i[y],sep='')
        y += 1