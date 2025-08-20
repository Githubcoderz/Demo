import re
 
string ='Welcome to Regular expression. Today is 18-07-2025' #text or string
pattern = r'\d{2}' 

if re.match(pattern, string):
        print('2 Digit Number found in string')
else:
    print('No 2 Digit number here')
 
print(f'{re.search(pattern, string)}')
print(f'{re.match(pattern, string)}')
print ("-" * 40)

'''
    findall will return a list
'''
 
string ='Welcome to Regular expression. Today is 18-07-2025 having 1, 2 or more digits' #text or string
pattern = r'\d{2,}' #regex
 
#print(f'{re.search(pattern, string)}')
print(f'{re.findall(pattern, string)}')
print ("-" * 40)

'''
\D --> Not a digits
\w --> Word character(a-zA-Z0-9_)
\W --> Not Word character(a-zA-Z0-9_)
'''

string = "Welcome to a Regular Expression performed on Day-11." \
"Today date- 18-0702025 " \
"it will be test "


pattern = r'\D{2,}' 
print(f'{re.findall(pattern, string)}')
print ("-" * 40)
pattern = r'\w+'
print (f'{re.findall(pattern, string)}')
print ("-" * 40)
pattern = r'\W{2,}'
print (f'{re.findall(pattern, string)}')
print ("-" * 40)

'''
    findall will return a list
'''
 
import re
 
string ='Welcome to Regular expression. Today is 18-07-2025 having 1, 2 or more digits' #text or string
pattern = r'(\d{2})-(\d{2})-(\d{4})' #regex
 
print(f'{re.search(pattern, string)}')
res = re.search(pattern, string)
print (f'Res: {res}')
print (f'Res: {res.span()}')
print (f'Res: {res.group()}')
print (f'Res: {res.groups()}')
 
#print(f'{re.findall(pattern, string)}')
print ("-" * 40)


'''
    findall will return a list
'''
import re
 
string ='is this what you are lookig for. Is is is in it' #text or string
pattern = r'i.' #regex
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='is this what you are lookig for. Is is is in it'
pattern = r'(i.)' #regex
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='is this what you are lookig for. Is is is in it'
pattern = r'i[ins]' #regex
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='is this what you are lookig for. Is is is in it'
pattern = r'i[^ins]' #regex
 
res = re.findall(pattern, string)
print(f'Res: {res}')

print ("-" * 40)

import re
 
string ='Is i in is iss isn ins ist isss issssss iss'
pattern = r'is?\s' #regex i 0 or 1 s' character
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='Is i in is iss isn ins ist isss issssss iss'
pattern = r'is{0,}\s' #regex i 0 or more s' character
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
 
string ='Is i in is iss isn ins ist isss issssss iss'
pattern = r'is*\s' #regex i 0 or more s' character
 
res = re.findall(pattern, string)
print(f'Res: {res}')
 
string ='Is i in is iss isn ins ist isss issssss iss'
pattern = r'is+\s' #regex i 1 or more s' character
 
res = re.findall(pattern, string)
print(f'Res: {res}')
print ("-" * 40)

import re
string = 'Hello World\nHello is the word\nWorld is also a word'
pat = r'^Hello'
 
res = re.findall(pat, string, re.MULTILINE)
print(f'1. Res: {res}')
 
string = '''Hello World
Hello is the reword
World is also a matchword'''
pat = r'word$'
 
res = re.findall(pat, string, re.MULTILINE)
print(f'1. Res: {res}')
print ("-" * 40)

'''
    finditer()
'''
import re
 
string = "Jan 1999, Feb 2005, Mar 2025"
for match in re.finditer(r"(\w{3}) (\d{4})", string):
    print(f"Month: {match.group(1)}, Year: {match.group(2)}")
 