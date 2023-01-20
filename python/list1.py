# lists
grocery = ["dragon fruit", "bread", "eggs"]
print(grocery)

print(grocery[0])    # print first element
print(grocery[-1])    # print the last element
print(grocery[2:5])   # print elements in the range
print(len(grocery))     # length
print(type(grocery))    # type of list

# insert
grocery.insert(2, "water")
print(grocery)

# append
grocery.append("orange")
print(grocery)

# extend
fruits = ["apple", "cherry"]
grocery.extend(fruits)
print(grocery)

# remove
grocery.remove("orange")
print(grocery)

# pop/remove2
grocery.pop(1)
print(grocery)

# delete by the index
del grocery[0]
print(grocery)

# replacing with one value
grocery[0:2] = ["chocolate"]
print(grocery)

# delete/clear entire list
grocery.clear()   # OR del grocery
print(grocery)