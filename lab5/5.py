import re
with open('original.txt.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()


pattern = r'a.+b$'
pattern1 = r'а.+б$'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern1, text)
print(matches)
print(matches2)
