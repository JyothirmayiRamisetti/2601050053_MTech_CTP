# Student Result Processing using Decomposition

##  Description

This project demonstrates the **Decomposition** technique of Computational Thinking using a simple Student Result Processing problem.

A college may have thousands of student marks and needs to calculate:
- Total marks
- Percentage
- Grades
- Class average
- Topper
- Pass percentage

Instead of solving the entire problem at once, it is divided into smaller and manageable tasks.

##  Computational Thinking Method

### Decomposition

**Decomposition** means breaking a large and complex problem into smaller, simpler tasks.

For Student Result Processing, the problem is divided into:

1. Enter student marks
2. Calculate total marks
3. Calculate percentage
4. Assign grades
5. Check pass/fail
6. Calculate class average
7. Find topper
8. Calculate pass percentage
9. Display the result

##  Example Dataset

| Student | Maths | Science | English |
|---------|------:|--------:|--------:|
| A       | 80    | 70      | 90      |
| B       | 60    | 65      | 70      |
| C       | 90    | 95      | 85      |

### Expected Results

- Student A → Total = 240, Percentage = 80%, Grade = A
- Student B → Total = 195, Percentage = 65%, Grade = B
- Student C → Total = 270, Percentage = 90%, Grade = A+
- Class Average = 235 marks
- Topper = Student C
- Pass Percentage = 100%

##  Technologies Used

- Python
- Basic Python concepts
- Dictionary
- Loops
- Conditional statements
- Built-in functions

##  Time Complexity

The overall **time complexity is O(n)**, where `n` is the number of students.

Each student is processed once to calculate the total, percentage, and grade. The other operations such as finding the topper, class average, and pass percentage also take O(n) time.

Therefore:

**Overall Time Complexity: O(n)**

### Space Complexity

The **space complexity is O(n)** because the total marks of all students are stored in a dictionary.

**Space Complexity: O(n)**
