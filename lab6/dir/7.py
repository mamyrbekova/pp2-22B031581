import os

first = 'first.txt'
second = 'second.txt'
with open(first, 'r') as f:
    x = f.read()

with open(second, 'w') as n:
    n.write(x)

print("done!")