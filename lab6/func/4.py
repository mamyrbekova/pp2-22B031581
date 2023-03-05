import math
import time

def squares(num, after):
    time.sleep(after / 1000.0)
    res = math.sqrt(num)
    return res

num = int(input())
after = int(input())

print(squares(num, after))