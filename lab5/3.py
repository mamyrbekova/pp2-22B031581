import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()


pattern = r'[a-z]+_[a-z]+'
pattern1 = r'[а-я]+_[а-я]+'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern1, text)
print(matches, matches2)