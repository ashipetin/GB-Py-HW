f_obj = open("new.txt", "r")
content = f_obj.readlines()
print(f"Строк в файле: {len(content)}")
for i in range(0,(len(content))):
    a = content[i]
    b = a.split()
    print(f"В {i+1} строке слов: {len(b)}")
f_obj.close
