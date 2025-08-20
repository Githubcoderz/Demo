import re
def find_dates(text):
    pattern = r'\d{2}-\d{2}-\d{4}'
    return re.findall(pattern, text)

print(find_dates("date 18-07-2025")) 