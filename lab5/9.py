import re

txt = "HelloThisIsPythonProgram"
pattern = r'([a-z])([A-Z])'

new = re.sub(pattern, r'\1 \2', txt)

print(new)