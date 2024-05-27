import math


class Figure:
    def __init__(self):
        self.square = -1
        self.perimentr = -1
    def squre(self):
        return -1
    def perimetr(self):
        return -1

    def compare_square(self, figure_another):
        return self.square()>figure_another.square()
    def compare_perimeneter(self, figure_another):
        return self.perimetr()>figure_another.perimetr()

class Rectangle(Figure):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def square(self):
        return self.a*self.b
    def perimetr(self):
        return 2*(self.a+self.b)

class Square(Rectangle):
    def __init__(self,a):
        Rectangle.__init__(self,a,a)

    def square(self):
        return Rectangle.square(self)
    def perimetr(self):
        return Rectangle.perimetr(self)

class Triangle(Figure):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a+self.b+self.c

    def square(self):
        p = self.perimetr()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class Cirlce(Figure):
    def __init__(self,a):
        self.a = a

    def perimetr(self):
        return 2*3.14*self.a

    def square(self):
        return 3.14*self.a*self.a

r = Rectangle(1,2)
r1 = Rectangle(2,2)
print(r.square())

sq = Square(4)
tr = Triangle(3,4,5)
c = Cirlce(41)

print(sq.square())

print(r.compare_square(r1))
print(c.compare_perimeneter(tr))
