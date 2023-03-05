import os
path = '/Users/aminamamyrbekova/PycharmProjects/pp2-22B031581/lab6/dir'

if os.access(path, os.F_OK):
    print("exists")
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("doesn't exist")


# if os.path.exists(path):
#     print(f'{path} exists')
#     print(os.path.basename(path))
#     print(os.path.dirname(path))
# else:
#     print(f'{path} does not exist')