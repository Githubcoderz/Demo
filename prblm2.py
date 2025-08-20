class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def fromString(cls, data):
        # Assumes format "Name Grade"
        name, grade = data.split()
        return cls(name, int(grade))

    @staticmethod
    def isPass(grade):
        return grade >= 50


if __name__ == '__main__':
    student1 = Student.fromString("Anand 55")

    print(f"Name: {student1.name}, Grade: {student1.grade}")

    print("Pass:", Student.isPass(student1.grade))