import json
with open("companies.txt", "r", encoding="utf8") as complist:
    lines = complist.readlines()
    profits = []
    dict_profits = {}
    dict_profits_avg = {}
    complist.seek(0)
    i = 0
    while i < len(lines):
        a = lines[i]
        a = a.split()
        dict_profits[f'{(" ".join(a[0:-2]))}'] = int(a[-2]) - int(a[-1])
        profit = int(a[-2]) - int(a[-1])
        if profit > 0:
            profits.append(profit)
        i += 1
dict_profits_avg["average profit"] = round(sum(profits) / len(profits))
anslist = [dict_profits,dict_profits_avg]
print(anslist)
with open("companies.json", "w") as write_f:
    json.dump(anslist, write_f)

# Для проверки получившегося файла
'''
with open ('companies.json', encoding="utf8") as read_f:
    data = json.load(read_f)
print(data)
'''