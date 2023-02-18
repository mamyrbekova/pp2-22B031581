import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()

pattern = r'a(bb|bbb)'
pattern2 = r'а(бб|ббб)'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern2, text)
print(matches, matches2)