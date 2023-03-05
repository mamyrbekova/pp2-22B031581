import os

path = '/Users/aminamamyrbekova/PycharmProjects/pp2-22B031581/lab6/dir/test.py'

if os.path.exists(path)and os.access(path, os.F_OK):
    os.remove(path)
    print("done!")
else:
    print("file does not exist")

