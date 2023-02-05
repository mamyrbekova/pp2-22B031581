def gen(a):
    i = 0
    while i <= a:
        if i % 2 == 0:
            yield i
        i += 1


a = int(input())
list = []
for i in gen(a):
    list.append(str(i))


print(",".join(list))