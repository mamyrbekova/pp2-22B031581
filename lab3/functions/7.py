def has_33(l1):
    s = ""
    for i in l1:
        s += str(i)
    return "33" in s


print(has_33([1, 3, 3, 4]))
