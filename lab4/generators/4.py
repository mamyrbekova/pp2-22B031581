def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


a = int(input())
b = int(input())
print(*squares(a, b))
