def evens(a):
    if a % 2 == 0:
        return True
    return False


def gen(a):
    for i in range(a + 1):
        if evens(i):
            yield i


a = int(input())
list = []
for i in gen(a):
    list.append(str(i))


print(",".join(list))