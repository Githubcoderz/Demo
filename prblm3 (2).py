import re

def replace_spaces(text):
    pattern = r'\s+'
    return re.sub(pattern, ' ', text)

print(replace_spaces("Let   see    a   spaced   string"))