klist = []
x = 1
while x > 0:
    tup = (x, {
    "Название":input(f"Введите название товара #{x}: "),
    "Цена":input(f"Введите цену товара #{x}: "),
    "Количество":input(f"Введите количество товара #{x}: "),
    "Ед":input(f"Введите единицы товара #{x}: ")
    })
    q = input("Есть еще товары? Y(y)/N(n): ")
    if q == "Y" or q == "y":
        x += 1
        klist.append(tup)
    elif q == "N" or q == "n":
        klist.append(tup)
        x = 0
    else:
        print("Error: unexpected value. Assuming negative reply...")
        klist.append(tup)
        x = 0
x = len(klist)
name = []
price = []
qty = []
pcs = []
z = 0
while x > 0:
    name.insert(0,[klist[z][1]["Название"]])
    price.insert(0,[klist[z][1]["Цена"]])
    qty.insert(0,[klist[z][1]["Количество"]])
    pcs.insert(0,[klist[z][1]["Ед"]])
    x -= 1
    z += 1
name = sum(name, [])
price = sum(price, [])
qty = sum(qty, [])
pcs = sum(pcs, [])
# pcs_unique = []
# [pcs_unique.append(g) for g in pcs if g not in pcs]
# Так можем сделать, если хотим, чтоб не повторялись единицы (шт.),
# как в примере.
# Но такое решение вижу нелогичным и ненужным.
warehouse = {"Название": name,"Цена": price,"Количество": qty,"Ед": pcs}
print(warehouse)
