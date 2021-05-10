f_obj = open("new_f.txt", 'w')
a = 1
while a > 0:
    i = input("Введите строки, для прекращения отправьте пустую: ")
    if i == "":
        a = 0
    f_obj.write(i)
    f_obj.write('\n')
f_obj.close
