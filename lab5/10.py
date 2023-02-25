import re

s = "CamelCaseString"
def camel(s):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake = pattern.sub('_', s).lower()
    return snake


print(camel(s))