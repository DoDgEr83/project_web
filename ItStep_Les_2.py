class Student:
    def __init__(self, age: int, grades: list):
        self.average = None
        self.age = age
        self.grades = grades

    def calculate_average(self, inplace=False):
        avarage = sum(self.grades) / len(self.grades)
        if inplace:
            self.average = avarage
        return avarage

    @classmethod
    def creat_simple_student(cls):
        return cls(15, [5,5])


student_1 = Student(11, [5, 6])

print(student_1.calculate_average())

ss = Student.creat_simple_student()

for student in (student_1, ss):
    print(student.calculate_average())