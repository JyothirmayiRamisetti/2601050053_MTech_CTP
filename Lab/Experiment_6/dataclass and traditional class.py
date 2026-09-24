from dataclasses import dataclass

class Student:
    def __init__(self, name: str, age: int, marks: float):
        self.name = name
        self.age = age
        self.marks = marks

@dataclass
class StudentData:
    name: str
    age: int
    marks: float

student1 = Student("Anu", 22, 85.5)
student2 = StudentData("Ravi", 23, 90.0)

print(student1.name, student1.age, student1.marks)
print(student2)
