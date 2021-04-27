def profile(**kwargs):
    return kwargs
a = profile(name = input("Введите имя: "),
lastname = input("Введите фамилию: "),
year = input("Введите год рождения: "),
city = input("Введите город проживания: "),
email = input("Введите e-mail: "),
phone = input("Введите номер телефона: "))
print(a)
