import re
s = "PythonProgram"
def split(s):
    x = re.findall('[A-Z][^A-Z]*', s)
    return " ".join(x)


print(split(s))