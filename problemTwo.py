dd, mm, yyyy = 3, 7, 2025
c, y = yyyy // 100, yyyy % 100

m = mm + 10 if mm <= 2 else mm - 2 #condition #1
y = y - 1 if m >= 11 else y  # condition #2

w = int(dd + (2.6 * m - 0.2) + y + y //4 + c // 4 - 2 * c ) % 7
print(f'w value for {dd}/{mm}/{yyyy} is {w}')