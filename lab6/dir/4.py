import os

path = '/Users/aminamamyrbekova/PycharmProjects/pp2-22B031581/lab5/file.txt'
with open(path, 'r') as f:
    cnt = 0
    for line in f:
        cnt += 1

print(cnt)