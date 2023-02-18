import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()


pattern = r'[A-Z][a-z]+'
pattern2 = r'[А-Я][а-я]+'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern2, text)
print(matches, matches2)