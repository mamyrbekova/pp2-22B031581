def gen(a):
    for i in range(a, -1, -1):
        yield i


print(*gen(int(input())))