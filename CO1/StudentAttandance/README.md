
Student Attendance Management System

Description

This project contains a Python script that implements a Student Attendance Management System. The system stores student attendance details, calculates attendance percentages, identifies students whose attendance is below 75%, finds the student with the highest attendance, and calculates the average attendance of the class.

Algorithm

The script uses functions and basic data structures to manage student attendance. The step-by-step algorithm is as follows:

Initialize Student Records: Create an empty list to store the details of all students.

Add Student: Ask the user to enter the student's name, total number of classes conducted, and number of classes attended.

Validate Input: Check whether the entered values are valid. The attended classes must not be greater than the total number of classes.

Calculate Attendance: Calculate the student's attendance percentage using the formula:

Attendance Percentage = (Classes Attended / Total Classes) × 100

Store Details: Store the student's name, total classes, attended classes, and attendance percentage.

Display Records: Display all students along with their total classes, attended classes, and attendance percentage.

Find Students Below 75%: Check the attendance percentage of every student. If it is less than 75%, display that student.

Find Highest Attendance: Compare the attendance percentages of all students and display the student or students with the highest attendance.

Calculate Class Average: Add the attendance percentages of all students and divide the total by the number of students to calculate the class average.

Not Found: If there are no student records available, display a message indicating that no records are available.

Input and Output

Input

Enter choice: 1

Enter student name: Anil

Enter total classes conducted: 40

Enter classes attended: 34

Output

Student Anil added successfully.
Attendance: 85.00%

Enter choice: 2

Output

Name                Total     Attended    Attendance
------------------------------------------------------
Anil                40        34          85.00%
