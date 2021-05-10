from functools import reduce
dict = {}
text = open("schedule.txt","r")
a = text.readlines()
text.seek(0)
for i in range(0,len(a)):
    b = text.readline()
    b = b.split()
    num = []
    for t in range(0,len(b)):
        if "(" in b[t]:
            c = b[t]
            c = c.split("(")
            num.append(c[0])
    lesson = b[0]
    lesson = lesson[:-1]
    dict[f'{lesson}']=int(reduce(lambda x,y:(int(x)+int(y)),num))
print(dict)
