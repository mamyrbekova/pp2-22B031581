# l = list(map(int, input().split()))
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = int((l // 2) + 1)
def prm(l):
    for i in range(2, k):
        primes = list(filter(lambda x: x % i == 0, l))

    print(primes)


prm(l)