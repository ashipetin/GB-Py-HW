class Matrix:
    def __init__(self, matlist):
        a = ""
        self.matlist = matlist
    def __str__(self):
        a = ""
        for i in range(0,len(self.matlist)):
            a = a + str(f"{self.matlist[i]}\n")
        return a
    def __add__(self, other):
        a = ""
        for i in range(0,len(self.matlist)):
            a = a + str(f"{[x+y for x,y in zip(self.matlist[i],other.matlist[i])]}\n")
        return a

ex1 = Matrix([[1,2,3,4],[4,6,7,4],[9,3,6,4]])
ex2 = Matrix([[3,2,1,4],[1,6,4,4],[4,2,1,4]])
print(ex1)
print(ex2)
print(ex1+ex2)
