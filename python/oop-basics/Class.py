class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


Abdul_Aziz = Student("Abdul_Aziz", 29, 90)
Munshi_Saju = Student("Munshi_Saju", 29, 60)
Masum_Miraj = Student("Masum_Miraj", 28, 99)

Bsc = Course("Bsc", 2)
Bsc.add_student(Abdul_Aziz)
Bsc.add_student(Munshi_Saju)
print(Bsc.get_average_grade())
Bsc.add_student(Masum_Miraj)

print(Bsc.get_average_grade())



















