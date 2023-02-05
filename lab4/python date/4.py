from datetime import datetime
y, m, d, h, min, s = map(int, input().split())
y1, m1, d1, h1, min1, s1 = map(int, input().split())
d = datetime(y, m, d, h, min, s)
d2 = datetime(y1, m1, d1, h1, min1, s1)
print((d - d2).total_seconds())