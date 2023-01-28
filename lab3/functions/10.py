# l = list(map(int, input().split()))
#
#
# def unique(l):
#     for i in range(len(l)):
#         if l[i] != l[i + 1]:
#             print(l[i])
#
#
# l.sort()
# l.reverse()
# unique(l)


def f(l):
    x = []

    for a in l:

        if a not in x:
            x.append(a)

    return x


print(f([1, 2, 3, 3, 3, 3, 4, 5, 2]))
