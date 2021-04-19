timesec = int(input("Введите время в секундах:"))
sec = timesec % 60
min = timesec % 3600 // 60
hour = timesec // 3600
print(f"{hour}:{min}:{sec}")
