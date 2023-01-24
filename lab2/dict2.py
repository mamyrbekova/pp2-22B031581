# loop
things = {
    "brand": "apple",
    "year": 2020,
    "colors": ["red", "purple", "black"],
}
# keys  or  (for x in dict3.values/keys())
for x in things:
    print(x)

# values
for x in things:
    print(things[x])

# items
for x, y in things.items():
    print(x, y)

# copy  or  dict(dict4)
dict4 = things.copy()
print(dict4)

# dict in dict
fam = {
    "mom": {
        "name": "Elly",
        "year": 1975
    },
    "dad": {
        "name": "John",
        "year": 1973
    },
    "child": {
        "name": "Emily",
        "year": 2000
    }
}
print(fam)


# fromkeys(key, value)
x = ('key1', 'key2', 'key3')
y = 0
dict5 = dict.fromkeys(x, y)
print(dict5)

# setdefault
z = things.setdefault("model", "iphone")
print(z)

