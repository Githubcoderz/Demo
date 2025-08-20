import calendar
import datetime


month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

date = datetime.date(year, month, 1)
weekday = date.weekday()


w = (weekday + 1) % 7

print(f"\n1-{month}-{year} --> w value => {w}\n")


print("Su Mo Tu We Th Fr Sa")


num_days = calendar.monthrange(year, month)[1]

current_pos = w
for _ in range(w):
    print("   ", end="")  

for day in range(1, num_days + 1):
    print(f"{day:2d} ", end="")
    current_pos = (current_pos + 1) % 7
    if current_pos == 0:
        print()

print()
