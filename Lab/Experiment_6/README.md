# Experiment 6 – Dataclass and Traditional Class

## Aim

Implement a **Student data model** using both a traditional Python class and a dataclass, and compare their implementations.

---

## Algorithm / Procedure

1. Create a traditional `Student` class.
2. Define the attributes and constructor using `__init__()`.
3. Create an equivalent `StudentData` dataclass.
4. Define the same attributes using type hints.
5. Create objects using both approaches.
6. Display the object information.
7. Compare the implementations.

---

## Program

```python
from dataclasses import dataclass


# Traditional Class
class Student:
    def __init__(self, name: str, age: int, marks: float):
        self.name = name
        self.age = age
        self.marks = marks


# Dataclass
@dataclass
class StudentData:
    name: str
    age: int
    marks: float


# Create objects
student1 = Student("Anu", 22, 85.5)
student2 = StudentData("Ravi", 23, 90.0)


# Display student details
print(student1.name, student1.age, student1.marks)
print(student2)
```

---

## Output

```text
Anu 22 85.5
StudentData(name='Ravi', age=23, marks=90.0)
```

---

## Explanation

### Traditional Class

The traditional class requires an explicit constructor:

```python
class Student:
    def __init__(self, name: str, age: int, marks: float):
        self.name = name
        self.age = age
        self.marks = marks
```

The `__init__()` method initializes the object's attributes manually.

### Dataclass

The dataclass is created using:

```python
@dataclass
class StudentData:
    name: str
    age: int
    marks: float
```

The `@dataclass` decorator automatically generates commonly required methods such as `__init__()` and `__repr__()`.

Therefore, less code is required compared with a traditional class.

---

## Comparison

| Feature                  | Traditional Class        | Dataclass               |
| ------------------------ | ------------------------ | ----------------------- |
| Constructor              | Written manually         | Automatically generated |
| `__repr__()`             | Usually written manually | Automatically generated |
| Code length              | More                     | Less                    |
| Type hints               | Optional                 | Commonly used           |
| Suitable for data models | Yes                      | Yes                     |
| Readability              | Good                     | Very good               |

---

## Inference & Analysis

Dataclasses reduce the amount of boilerplate code required when creating classes primarily used for storing data. They automatically provide useful methods such as `__init__()` and `__repr__()`, making the implementation shorter and easier to read.

The traditional class provides more manual control, while a dataclass is convenient when the main purpose of a class is to store and represent structured data.

---

## Result

Thus, a **Student data model** was successfully implemented using both a traditional Python class and a dataclass, and their implementations were compared.

