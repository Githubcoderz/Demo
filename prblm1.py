class Employee:
    raise_percent = 1.05  

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def applyRaise(self):
        self.salary *= self.raise_percent  

    @classmethod
    def setRaisePercent(cls, amount):
        cls.raise_percent = amount  

    @staticmethod
    def isWorkday(day):
        return day.lower() not in ('saturday', 'sunday')


if __name__ == '__main__':
    emp1 = Employee("Anand sharma ", 50000)
    emp2 = Employee("Bobby " , 40000)

    # Print initial details
    print(f"Name: {emp1.name}, Salary: {emp1.salary}")
    print(f'Name: {emp2.name}, Salary: {emp2.salary}')

    emp1.applyRaise()
    print(f"After 1st raise Name: {emp1.name}, Salary: {emp1.salary}")
    emp2.applyRaise()
    print(f"After 1st raise Name: {emp2.name}, Salary: {emp2.salary}")

    # Change raise percent
    Employee.setRaisePercent(1.10)

    emp1.applyRaise()
    print(f"After 2nd raise Name: {emp1.name}, Salary: {emp1.salary}")
    emp2.applyRaise()
    print(f"After 2nd raise Name: {emp2.name}, Salary: {emp2.salary}")

    # Check if Sunday is a workday
    print("Is Sunday a workday?", Employee.isWorkday("Sunday"))