class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def toPerson(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

    def __str__(self):
        return f'Name: {self.name}\t\tAge: {self.age}'


class Employee(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f'{super().__str__()}\tSalary: {self.grade}'

#Extend the Person class with a Student class.			
#class Student(Person): #Syntax for inheritance 
#self.grade --> have data member

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def __str__(self):
        return f'{super().__str__()}\tCourse: {self.course}'
if __name__ == '__main__':
    emp = Employee('Anand', 50, 200000)
    print("Employee Info:")
    print(emp)

    stu = Student('Ravi', 20, 'B.Tech CSE')
    print("\nStudent Info:")
    print(stu)