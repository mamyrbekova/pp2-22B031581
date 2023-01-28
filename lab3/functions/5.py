def permut(string, i=0):
    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]

        permut(words, i + 1)


print(permut('yup'))