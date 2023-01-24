# insert
set0 = {"a", "b", "c"}
set1 = {1, 2, 3}

final = set0.union(set1)
print(final)

set0.update(set1)
print(set0)

# intersection
x = {"samsung", "apple", "xiaomi"}
y = {"apple", "poco", "oppo"}
x.intersection_update(y)
print(x)

# delete the common
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
a.symmetric_difference_update(b)
print(a)
