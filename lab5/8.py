import re
txt = "PythonProgram"
def split(s):
    x = re.findall('[A-Z][^A-Z]*', txt)
    return " ".join(x)


print(split(txt))