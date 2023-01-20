# elif
a = 67
b = 67
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")

# elif,else
x = 190
y = 45
if y > x:
    print("Y is greater than X")
elif x == y:
    print("X and Y are equal")
else:
    print("X is greater than Y")

# short one "if"
if x > y: print("X is greater than Y")

# short one "if, else"
print("T") if x > y else print("F")

print("T") if a > b else print("=") if a == b else print("B")

# and
if x > y and a == b:
    print("both conditions are true")

# nested if
x = 93

if x > 50:
    print("Above fifty,")
    if x > 70:
        print("and also above 70!")
    else:
        print("but not above 70.")
