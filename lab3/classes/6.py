l = list(map(int, input().split()))
primes = range(2, 100000)
s = set()
s1 = set(l)
for i in range(2, len(l)):
    primes = filter(lambda x: x == i or x % i, primes)
    for j in primes:
        s.add(j)


print(*s.intersection(s1))