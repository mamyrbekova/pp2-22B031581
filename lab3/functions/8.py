def spy_game(name):
    for i in range (len(name)-2):
        if name[i] == "0" and name[i+1] == "0" and name[i+2] == "7":
            print("spy_game {} --> True".format(name))
        else:
            print("spy_game {} --> False". format(name))

name = [int(i) for i in input().split()]
spy_game(name)