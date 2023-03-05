import os

path = '/Users/aminamamyrbekova/PycharmProjects/pp2-22B031581/lab5/file.txt'

if os.access(path, os.F_OK):
    print("yes, it exists")
else:
    print("no, it doesn't exist")

if os.access(path, os.R_OK):
    print("yes, readable")
else:
    print("no, can't read")

if os.access(path, os.R_OK):
    print("yes, writable")
else:
    print("no, can't write")

if os.access(path, os.X_OK):
    print("yes, can execute")
else:
    print("no, can't")
