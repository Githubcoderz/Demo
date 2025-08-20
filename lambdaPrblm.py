#REMOVE EMPTY STRINGS
strings = ['hello', '', 'world', '', 'VSCode']
result = list(filter(lambda x: x, strings)) 
print(result)

#MAX string
result = max(strings, key=lambda x: len(x)) 
print(result)


strings = ['apple', 'banana', 'orange', 'grape', 'umbrella']
result = list(filter(lambda x: x[0].lower() in 'aeiou', strings))  
print(result)


marks = [54, 69, 89, 20, 40, 55]

result = list(map(lambda x: "Pass" if x >= 40 else "Fail", marks))
print(result)