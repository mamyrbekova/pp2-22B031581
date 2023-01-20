# sort
colors = ["blue", "orange", "yellow", "green"]
colors.sort()
print(colors)

# sort numbers
numbers = [10, 560, 34, 1, 67]
numbers.sort()
print(numbers)

# sort in reverse
colors.sort(reverse=True)
print(colors)


# Sort the list based on how close the number is to 30
def func(n):
    return abs(n - 30)


numbers.sort(key=func)
print(numbers)

# sort by uppercase/lowercase and reverse
list = ["mango", "Milk", "bread", "Cookie"]
list.sort(key=str.lower)
print(list)

list.reverse()
print(list)

# copy
newl = list.copy()
print(newl)

# adding
list1 = ["go", "the", "an"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)



