class Rectangle:
    def __init__(self, l, b):
        self.l, self.b = l, b

class Cuboid(Rectangle):
    def __init__(self, l=0, b=0, h=0):
        super().__init__(l, b)
        self.h = h
    def volume(a):
        return a.h * a.b * a.h
    def __le__(a, b):
        return a.volume() < b.volume()

c1 = Cuboid(10, 20, 30)
c2 = Cuboid(10, 3, 4)
print(f"c1<c2 : {c1<=c2}")
