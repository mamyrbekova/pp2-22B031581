import math


def trapezoid(h, a, b):
    s = ((a + b) / 2) * h
    return s


h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print("Expected Output: ", trapezoid(h, a, b))
