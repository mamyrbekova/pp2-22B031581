l = list(map(int, input().split()))
def filter_prime(l):
    if l == 0 or l == 1:
        return False
    for i in range(2, l // 2 + 1):
        if l % i == 0:
            return False
    return True

def check(l):
    for i in l:
        if filter_prime(i):
            print(i)


check(l)




