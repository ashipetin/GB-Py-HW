salary = open("salary.txt", "r")
content = salary.readlines()
salary.close()
salarylist = []
if len(content) > 0:
    print("Фамилии сотрудников с окладом менее 20000: ")
for i in range(0,len(content)):
    a = content[i]
    b = a.split()
    if int(b[1]) < 20000:
        print(b[0])
    salarylist.append(int(b[1]))
print("Средний оклад: ",round(sum(salarylist)/len(salarylist)))
