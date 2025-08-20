# main.py

from OOPmodel.EmployeeOne import Manager, Developer, Intern

if __name__ == '__main__':
    staff = [
        Manager("Anand", "anand@xyz.com", 90000),
        Developer("Bobby", "bobby@xyz.com", 60000),
        Intern("Chanti", "chanti@xyz.com", 5000)
    ]

    for emp in staff:
        print(f"{emp.name} bonus: {emp.calculateBonus()}")