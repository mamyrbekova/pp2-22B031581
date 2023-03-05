import os

path = '/Users/aminamamyrbekova/PycharmProjects/pp2-22B031581/lab4'


print("Directories:")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)


print("\nFiles:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)


print("\nAll directories and files:")
for all in os.listdir(path):
    print(all)
