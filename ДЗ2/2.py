l = (input("Введите элементы списка через запятую")).split(",")
i = 0
while i < len(l):
    try: l[i], l[i+1] = l[i+1], l[i]
    except: pass
    i += 2
print(l)