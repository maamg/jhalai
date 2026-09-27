class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


munna = Student("Munna", 25, 3.25)

print(munna.grade)
print(munna.get_grade())
