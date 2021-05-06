#coding:utf-8
dict = {'One':'Один','Two':'Два','Three':'Три', 'Four':'Четыре'}
digits = open("digits.txt", "r")
result = open("digresult.txt", "w")
lines = digits.readlines()
digits.seek(0)
i = 0
while i < len(lines):
    lsplit = lines[i].split()
    string = (dict.get(lsplit[0]),lsplit[1],lsplit[2])
    result.write(" ".join(string)+"\n")
    i += 1
digits.close()
result.close()

# Та же самая конструкция, не работала, если я использовал для итерации:
# for i in range(0,len(digits.readlines()):
# Строки выводились пустые. Если не трудно, расскажите, почему
# Спасибо заранее