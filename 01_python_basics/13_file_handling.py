# ============================================================
# PYTHON BASICS — FILE HANDLING
# ============================================================


# 1. FILE HANDLING — SYNTAX- Open a file: file = open("filename.txt", "mode")
# Common modes: "r" → Read, "w" → Write, "a" → Append,"x" → Create a new file
# Example: file = open("student.txt", "r")

# Using with open(): with open("student.txt", "r") as file: content = file.read()

# Read the entire file: file.read()

# Read one line: file.readline()

# Read all lines: file.readlines()

# Write to a file: with open("student.txt", "w") as file: file.write("Hello Python")

# Append to a file: with open("student.txt", "a") as file: file.write("\nNew Student")


# 2. NOTES

# File handling allows Python programs to work with files stored on the computer.
# The main operations are:Create, Read, Write, Append, Close.
# "r" means read. The file must already exist.
# "w" means write. It creates a file if it does not exist. If the file already exists, its previous contents can be overwritten.
# "a" means append. New content is added to the end of the file.
# "x" means create. It creates a new file and produces an error if the file already exists.
# The with statement is recommended because Python automatically closes the file after the block finishes.
# Example: with open("student.txt", "r") as file:content = file.read()

# 3. READING FILES — SYNTAX
# Read complete file: with open("student.txt", "r") as file: content = file.read()
#  print(content)

# Read one line: with open("student.txt", "r") as file: line = file.readline()
#  print(line)

# Read all lines: with open("student.txt", "r") as file: lines = file.readlines()
# print(lines)

# 4. WRITING FILES — SYNTAX
# Write text: with open("student.txt", "w") as file: file.write("Python is easy to learn.")
# Write multiple lines: with open("student.txt", "w") as file:
#     file.write("Python\n")
#     file.write("SQL\n")
#     file.write("Power BI\n")
# 5. APPENDING FILES — SYNTAX: Add new content without removing existing content:
# with open("student.txt", "a") as file:
#     file.write("\nPandas")

# 6. PRACTICE QUESTIONS

# Q1. CREATE AND WRITE A FILE
# Create a file called: "student.txt"
# Write the following text into the file: "Python Student". Use the "w" mode.
file = open("student.txt", "w")
file.write("Python Student")
file.close()

# Q2. WRITE MULTIPLE LINES
# Create a file called: "courses.txt"
# Write the following courses into the file:Python,SQL, Power BI, Excel
# Each course should appear on a separate line.
file = open("couurses.txt", "w")
file.write("SQL")
file.write("Python")
file.write("Power BI")
file.write("Excel")
file.close()

# Q3. READ A FILE
# Using the "courses.txt" file from Q2: Open the file in read mode.
# Read the complete contents. Print the contents.
with open("courses.txt", "r") as file:
    contents = file.read()
print(contents)

# Q4. READ ONE LINE
# Create a file called:"students.txt". Add at least three student names, each on a separate line.
# Open the file and use readline() to read only the first line.
# Print the result.
with open("students.txt", "w") as file:
    file.write("Aman\n")
    file.write("Riya\n")
    file.write("Rahul\n")
with open("students.txt", "r") as file:
    first_line = file.readline()
print(first_line)

# Q5. READ ALL LINES
# Using the "students.txt" file: Use readlines() to read all lines.
# Store the result in a variable called `students`. Print the variable.
with open("students.txt", "r") as file:
    students = file.readlines()
print(students)

# Q6. APPEND DATA
# Using the "students.txt" file: Add two more student names to the end of the file.
# Use append mode "a". Then read the file again and print all students.
with open("students.txt", "a") as file:
    file.write("Priya\n")
    file.write("Neha\n")
with open("students.txt", "r") as file:
    students = file.read()
print(students)

# Q7. COUNT STUDENTS
# Create a file called: "students.txt". Store at least five student names, one name per line.
# Read the file. Count how many students are present. Store the result in `student_count`.
# Print the count.
with open("students.txt", "w") as file:
    file.write("Aman\n")
    file.write("Riya\n")
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Neha\n")
with open("students.txt", "r") as file:
    students = file.readlines()
student_count = len(students)
print("Total students:", student_count)

# Q8. PROCESS FILE CONTENT
# Create a file called: "marks.txt". Store these marks, one per line:
# 75, 82, 91, 68, 88
# Read the file. Convert each mark from a string into an integer.
# Calculate:total marks,average marks. Print both results.
with open("marks.txt", "w") as file:
    file.write("75\n")
    file.write("82\n")
    file.write("91\n")
    file.write("68\n")
    file.write("88\n")
with open("marks.txt", "r") as file:
    marks = file.readlines()
marks = [int(mark.strip()) for mark in marks]
total_marks = sum(marks)
average_marks = total_marks / len(marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Q9. STUDENT FILE ANALYSIS
# Create a file called: "student_data.txt". Store student records in the following format:
# Aman,75, Riya,82, Rahul,91, Priya,68, Neha,88
# Read the file. Use Python to:
# 1. Read each line, 2. Separate the student name and marks, 3. Convert marks into integers.
# 4. Find the highest marks, 5. Calculate the average marks.
# Print the results clearly.
with open("student_data.txt", "w") as file:
    file.write("Aman,75\n")
    file.write("Riya,82\n")
    file.write("Rahul,91\n")
    file.write("Priya,68\n")
    file.write("Neha,88\n")
with open("student_data.txt", "r") as file:
    lines = file.readlines()
students = []
for line in lines:
    name, marks = line.strip().split(",")
    marks = int(marks)
    students.append((name, marks))
highest_student = max(students, key=lambda student: student[1])
average_marks = sum(student[1] for student in students) / len(students)
print("Highest Marks:", highest_student[0], highest_student[1])
print("Average Marks:", average_marks)


# Q10. MINI CHALLENGE ⭐
# Create a simple Student Record program using files.Create a file called: "student_records.txt"
#Store at least five students using this format: Name,Department,Marks
# Example:Aman,IT,85. Your program should:
# 1. Create/write the student records to the file.
# 2. Read the file.
# 3. Display all student records.
# 4. Calculate the total number of students.
# 5. Calculate the average marks.
# 6. Find the student with the highest marks.
# 7. Find the student with the lowest marks.
# 8. Append one new student to the file.
# 9. Read the updated file.
# 10. Display the updated student records.
# Use:
# - with open()
# - read()
# - readlines()
# - write()
# - append mode
# - loops
# - type conversion
# Do not use Pandas for this challenge.
# Solve it using basic Python file handling.
# 1. Create and write student records
with open("student_records.txt", "w") as file:
    file.write("Aman,IT,85\n")
    file.write("Riya,HR,78\n")
    file.write("Rahul,Finance,92\n")
    file.write("Priya,IT,88\n")
    file.write("Neha,HR,75\n")
# 2. Read the file
with open("student_records.txt", "r") as file:
    records = file.readlines()
# 3. Display all student records
print("Student Records:")
students = []
for record in records:
    name, department, marks = record.strip().split(",")
    marks = int(marks)
    students.append((name, department, marks))
    print(name, department, marks)
# 4. Total number of students
student_count = len(students)
print("\nTotal Students:", student_count)
# 5. Average marks
total_marks = sum(student[2] for student in students)
average_marks = total_marks / student_count
print("Average Marks:", average_marks)
# 6. Student with highest marks
highest_student = max(students, key=lambda student: student[2])
print(
    "Highest Marks:",
    highest_student[0],
    highest_student[2]
)
# 7. Student with lowest marks
lowest_student = min(students, key=lambda student: student[2])
print(
    "Lowest Marks:",
    lowest_student[0],
    lowest_student[2])
# 8. Append one new student
with open("student_records.txt", "a") as file:
    file.write("Karan,IT,90\n")
# 9. Read the updated file
with open("student_records.txt", "r") as file:
    updated_records = file.readlines()
# 10. Display updated student records
print("\nUpdated Student Records:")
for record in updated_records:
    name, department, marks = record.strip().split(",")
    print(name, department, marks)