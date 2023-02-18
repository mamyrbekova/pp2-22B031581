import re

txt = "CamelCaseString"
def camel(txt):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake = pattern.sub('_', txt).lower()
    return snake


print(camel(txt))