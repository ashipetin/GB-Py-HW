my_list = [1, 300, 2, 43, 65, 3, 65, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 66]
new_list = [my_list[i] for i in range(1,len(my_list)) if my_list[i-1]<my_list[i]]
print(new_list)
