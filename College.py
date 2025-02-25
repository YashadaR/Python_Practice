class Student:
    college_name = "Imperial college"  # class variable

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = []

    def add_marks(self, marks):
        self.marks = (marks)

S1 = Student("ABC", 22, [30, 45, 50])
print(S1.name, S1.age, S1.marks)