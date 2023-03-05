import os
import string

alphabet = 'files'
if not os.path.exists(alphabet):
    os.makedirs(alphabet)

for l in string.ascii_uppercase:
    name = os.path.join(alphabet, l + '.txt')

    with open(name, 'w') as f:
        pass

    print("done!")
