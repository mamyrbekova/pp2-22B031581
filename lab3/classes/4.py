import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def distance(self, p1):
        a = p1.x - self.x
        b = p1.y - self.y
        return math.sqrt(a ** 2 + b ** 2)


p = Point(1, 2)
p2 = Point(3, 3)
print(p.show())
p.move(5, 6)
print(p.show())
print(p.distance(p2))