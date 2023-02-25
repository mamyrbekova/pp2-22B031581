import re

s = "HelloThisIsPythonProgram"
pattern = r'([a-z])([A-Z])'

new = re.sub(pattern, r'\1 \2', s)

print(new)