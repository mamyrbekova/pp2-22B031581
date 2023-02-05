import math
def radians(d):
    r = (d * math.pi)/180
    return r


d = int(input("Input degree: "))
print("Output radian: ", radians(d))