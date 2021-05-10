#A
print("Task A:")
from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

#B
print("Task B:")
from itertools import cycle
mylist = ["a","b","c","d",10,20,30,["t","x","h"]]
c = 0
for el in cycle(mylist):
    if c > 30:
        break
    print(el)
    c += 1