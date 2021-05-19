class Cell():
    def __init__(self, x):
        self.x=x
    def __add__(self, other):
        return self.x + other.x
    def __sub__(self, other):
        if self.x > other.x:
            return self.x - other.x
        else:
            return "Can not substract"
    def __mul__(self, other):
        return self.x * other.x
    def __truediv__(self, other):
        return self.x//other.x
    def make_order(self,row):
        res = ""
        if row >= self.x:
            return "*" * row
        elif row < self.x:
            i = self.x
            while i > row:
                i = i - row
                res = res + ("*" * row) + "\n"
            res = res + ("*" * i)
        return res
a=Cell(13)
b=Cell(4)
print(a/b)
print(a+b)
print(a-b)
print(a*b)
print(a.make_order(3))