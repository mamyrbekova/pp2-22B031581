things = ["bed", "pillow", "phone"]
for x in things:
    print(x)

for i in range(len(things)):
    print(things[i])

# while loop
i = 0
while i < len(things):
    print(things[i])
    i = i + 2  # go through all indexes by a formula

# A short hand for loop that will print all items in a list
[print(x) for x in things]

# List Comprehension
new = []
for x in things:
    if "o" in x:
        new.append(x)
print(new)  # outputs elements that contains letter "o"


# Only accept items that are not "pillow"
new = [x for x in things if x != "pillow"]
print(new)

# Set the values in the new list to upper case
new = [x.upper() for x in things]
print(new)

# return "chair" instead of "bed"
new = [x if x != "bed" else "chair" for x in things]
print(new)



