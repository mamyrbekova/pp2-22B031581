# booleans
print(10 < 9)
print(9 == 9)
print(5.4 != 5)  # check if the statement true or false

# if/else
x = 30
y = 100

if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")


# return
def func():
    return True


if func():
    print("yass")
else:
    print("nope(")

# data type checking
a = 50
print(isinstance(a, int))  # is "a" integer?
print(isinstance(a, float))  # is "a" float?
print(isinstance(a, complex))  # is "a" complex?

# logical operators
a = 6
print(a > 4 and a < 9)  # Returns True if both statements are true
print(a > 5 or a > 9)  # Returns True if one of the statements is true
print(not (a > 3 and a < 10))  # Reverse the result, returns False if the result is true
