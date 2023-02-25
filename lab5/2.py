import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()

pattern = r'a(bb|bbb)'
pattern1 = r'а(бб|ббб)'

matches = re.findall(pattern, text)
matches1 = re.findall(pattern1, text)
print(matches, matches1)