class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length


class Rectangle(Shape):
    def __init__(self, length, weight):
        super().__init__(length)
        self.weight = weight

    def area(self):
        return super().area() * self.weight


p = Rectangle(2, 5)
print(p.area())



