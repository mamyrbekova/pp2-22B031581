weather = ("rainy", "cloudy", "sunny")

print(weather)
print(len(weather))    # length
print(type(weather))     # type
print(weather[1])        # print second item
print(weather[0:1])       # print in range

if "cloudy" in weather:
    print("Yes, 'cloudy' is in the weather tuple")

# convert the tuple into list
x = weather
y = list(x)
y[1] = "chilly"
x = tuple(y)
print(x)

# convert the tuple into list and add element
y = list(weather)
y.append("cold")
weather = tuple(y)
print(weather)

# add two tuples
y = ("warm",)
weather += y
print(weather)

# remove
y = list(weather)
y.remove("sunny")
weather = tuple(y)
print(weather)

# del/ will give an error cuz tuple doesnt exist
del weather
print(weather)










