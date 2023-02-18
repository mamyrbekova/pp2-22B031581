import re

with open('file.txt', 'r', encoding = "utf-8") as f:
    text = f.read()

new = re.sub(r'[ ,.]', ':', text)

with open('file.txt', 'w') as f:
    f.write(new)