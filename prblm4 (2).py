import re


def capital_words(text):
    pattern = r'\b[A-Z][a-zA-Z]'
    return re.findall(pattern, text)

print(capital_words("All words Should Be a Capital"))