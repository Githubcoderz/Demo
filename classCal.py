import calendar
from datetime import date

class MyDate:
    def __init__(self, dd, mm, yyyy):  # Constructor to initialize date
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def isLeap(self):
        return calendar.isleap(self.yyyy)

    def maxDays(self):
        return calendar.monthrange(self.yyyy, self.mm)[1]

    def monthName(self):
        return calendar.month_name[self.mm]

    def printCal(self, newMonth=0, newYear=0):
        if newMonth == 0:
            newMonth = self.mm
        if newYear == 0:
            newYear = self.yyyy
        print(calendar.month(newYear, newMonth))

    def printJulianCal(self, newMonth=0, newYear=0):
        if newMonth == 0:
            newMonth = self.mm
        if newYear == 0:
            newYear = self.yyyy
        print(calendar.TextCalendar(firstweekday=0).formatmonth(newYear, newMonth))

    def julianDay(self):
        given_date = date(self.yyyy, self.mm, self.dd)
        start_of_year = date(self.yyyy, 1, 1)
        return (given_date - start_of_year).days + 1


if __name__ == '__main__':
    obj = MyDate(16, 7, 2025)
    print("Is Leap Year?:", obj.isLeap())
    print("Max Days in Month:", obj.maxDays())
    print("Month Name:", obj.monthName())
    print("Julian Day:", obj.julianDay())
    print("Calendar:")
    obj.printCal()
    print("Julian Style Calendar:")
    obj.printJulianCal()