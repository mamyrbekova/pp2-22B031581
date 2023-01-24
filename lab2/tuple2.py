# unpacking
fruits = ("mango", "papaya", "kiwi")
(yellow, pink, green) = fruits
print(yellow)
print(pink)
print(green)

# output two elements which includes "*white"
veggies = ("carrot", "potato", "tomato", "onions", "garlic")
(orange, brown, red, *white) = veggies
print(orange)
print(brown)
print(red)
print(white)

# loops in the tuple
for x in fruits:
    print(x)

# while
i = 0
while i < len(veggies):
    print(veggies[i])
    i = i + 2

# multiply
newone = fruits * 2
print(newone)

# index of element/ count
x = veggies.index("garlic")
print(x)

y = veggies.count("onions")
print(y)


