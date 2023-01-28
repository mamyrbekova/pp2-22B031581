class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square:
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


p = Square(4)
print(p.area())
