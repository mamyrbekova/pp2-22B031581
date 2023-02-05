import math

num = int(input("Input number of sides: "))
sides = int(input("Input the length of a side: "))
area = num * (sides ** 2) / (4 * math.tan(math.pi / num))
print("The area of the polygon is: ", int(area))