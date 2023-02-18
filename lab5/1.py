import re
with open('original.txt', 'r', encoding = "utf-8") as f:
    text = f.read()


pattern = r'a(b*)'
pattern2 = r'а(б*)'

matches = re.findall(pattern, text)
matches2 = re.findall(pattern2, text)
print(matches, matches2)