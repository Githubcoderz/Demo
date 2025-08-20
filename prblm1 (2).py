import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return (re.match(pattern, email))

print(validate_email("wipro@test.com"))