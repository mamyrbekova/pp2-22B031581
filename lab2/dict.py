newdict = {
    "brand": "apple",           # string
    "year": 2020,               # int
    "colors": ["red", "purple", "black"],      # list
    "magnet charging": False          # bool
}
print(newdict)
print(newdict["year"])
print(len(newdict))
print(type(newdict))

# constructor
dict2 = dict(name = "Anna", age = 45, country = "USA")
print(dict2)

# keys
x = newdict.get("year")
print(x)

y = newdict.keys()
print(y)

newdict["model"] = "iphone"       # print keys() after the changes
print(y)

z = newdict.values()
print(z)

k = newdict.items()               # value pairs
print(k)

# if
if "year" in newdict:
    print("Yes")


# changes
newdict.update({"year": 2021})
print(newdict)

# pop
newdict.pop("magnet charging")
print(newdict)

# popitem(removes the last inserted item)
newdict.popitem()
print(newdict)

# del
del newdict["colors"]
print(newdict)

# clear
newdict.clear()
print(newdict)