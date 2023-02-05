def gen(a):
    i = 0
    while i <= a:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1


print(*gen(int(input())))
