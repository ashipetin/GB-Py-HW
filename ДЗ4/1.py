def income(x,y,z):
    return (x * y + z)
x = int(input("Введите выработку в часах: "))
y = int(input("Введите ставку в час: "))
z = int(input("Введите премию: "))
print(income(x,y,z))