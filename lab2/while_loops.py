# while
i = 1
while i < 5:
    print(i)
    i += 1

# break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)

# else
i = 1
while i < 8:
    print(i)
    i += 1
else :
    print("i is no longer less than 8")




