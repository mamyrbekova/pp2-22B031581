# arrays
types = ["titan", "gold", "silver"]
print(types)

x = types[0]
print(x)

types[1] = "metal"          # change the values
print(types)

y = len(types)
print(y)

for x in types:
    print(x)

# add
types.append("aluminium")
print(types)

# delete
types.pop(0)
print(types)

# extend
cars = ['Ford', 'BMW', 'Volvo']
types.extend(cars)
print(types)

# insert
types.insert(1, "copper")
print(types)

# reverse
types.reverse()
print(types)

# sort
types.sort()
print(types)