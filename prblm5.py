import re

def replacealldigits(text):
    pattern = r'\d'
    return re.sub(pattern, '*', text)

print(replacealldigits("Today's DATE: 18-07-2025"))