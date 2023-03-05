string = "Hello, This is Python program"

up = 0
low = 0

for char in string:
    if char.isupper():
        up += 1
    elif char.islower():
        low += 1


print("upper count: ", up)
print("lower count: ", low)
