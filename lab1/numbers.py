# equality
x = ["orange", "banana"]
y = x
z = ["orange", "banana"]

print(x is y)     # x is y, they are the same
print(x is z)     # x isn't z, because they are not the same list, even though they have the equal content
print(x == z)     # they have equal content, that's why they are EQUAL

print(x is not y)   # returns false, because they are the same list

print("orange" in x)   # checks elements presence
print("apple" in z)
print("banana" not in x)