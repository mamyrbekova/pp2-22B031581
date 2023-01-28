def histogram(l):
    l2 = []
    for i in l:
        l2.append("*" * i)
    return l2


# l = list(map(int, input().split()))
# l2 = histogram(l)
# print(l2, sep = '\n')

print(*histogram(list(map(int, input().split()))), sep = '\n')
