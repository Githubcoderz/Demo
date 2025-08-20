# OOPModel/EmployeeOne.py

from abc import ABC, abstractmethod
from OOPmodel.PersonOne import Person

class Employee(Person, ABC):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    @abstractmethod
    def calculateBonus(self):
        pass


class Manager(Employee):
    def calculateBonus(self):
        return self.salary * 0.20


class Developer(Employee):
    def calculateBonus(self):
        return self.salary * 0.10


class Intern(Employee):
    def calculateBonus(self):
        return 0