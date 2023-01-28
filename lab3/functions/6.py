s = input()


def rever(s):
    s_list = s.split()             # string to list
    reverse_list = s_list[:: -1]          # reverse the list
    reversed_s = " ".join(reverse_list)         # list to string
    print(reversed_s)


rever(s)