import re

with open('file.txt', 'r', encoding = "utf-8") as f:
    txt = f.read()

new = re.sub(r'[ ,.]', ':', txt)

with open('file.txt', 'w') as f:
    f.write(new)