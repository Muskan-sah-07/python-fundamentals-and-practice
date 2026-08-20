# ============================================================
# PYTHON BASICS — TUPLES
# ============================================================

# 1. TUPLES — SYNTAX
# A tuple is an ordered collection of items. Tuples are created using parentheses ().
# Example:students = ("Aman", "Riya", "Rahul", "Priya")

# A tuple can contain different data types: student = ("Muskan", 26, 85.5, True)
# Access an item using its index: tuple[index]
 #Example: print(students[0])
# Negative indexing: print(students[-1])
# Tuple slicing: tuple[start:end]
# Example:print(students[0:2])

# 2. NOTES

# Tuples are: Ordered
# - Immutable (cannot be changed after creation)
# - Allow duplicate values
# - Can contain different data types
# - Use parentheses ()

# Python uses zero-based indexing. The first item has index 0.
# Example: courses = ("Python", "SQL", "Power BI")
# Python   -> index 0, SQL      -> index 1, Power BI -> index 2
# Unlike lists, tuple items cannot be changed directly.
# Example: courses[0] = "Excel". This will cause an error because tuples are immutable.

# A tuple with only one item needs a comma: single_item = ("Python",)
# Without the comma, Python treats it differently: single_item = ("Python")

# 3. TUPLE METHODS — SYNTAX
# count(): Counts how many times an item appears.
# tuple.count(item)
# index(): Finds the position of an item.
# tuple.index(item)
# len(): Returns the number of items.
# len(tuple)

# 4. PRACTICE QUESTIONS

# Q1. CREATE A TUPLE. 
# Create a tuple called `courses` containing: "Python", "SQL", "Power BI", "Excel"
# Print the tuple.
courses = ("Python", "SQL", "Power BI", "Excel")
print(courses)
print(type(courses))

# Q2. ACCESS TUPLE ITEMS
# Create: students = ("Aman", "Riya", "Rahul", "Priya", "Neha")
# Print:the first student, the third student,the last student.
students = ("Aman", "Riya", "Rahul", "Priya", "Neha")
print(students[0], students[2], students[-1])

# Q3. NEGATIVE INDEXING
# Create a tuple containing five programming languages. 
# Use negative indexing to print:the last language,the second-last language
code = ("Python","Sql","C","C++","Java")
print(code[-2::])

# Q4. TUPLE LENGTH
# Create a tuple containing six course names. Use len() to find the number of courses.
# Store the result in `course_count`. Print it.
course = ("Python","Sql","C","C++","Java","Excel")
print(len(course))

# Q5. TUPLE SLICING
# Create: numbers = (10, 20, 30, 40, 50, 60)
# Use slicing to print: the first three numbers, the last three numbers, numbers from index 1 to 4.
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[0:3], numbers[-3:], numbers[1:5])

# Q6. COUNT ITEMS
# Create: departments = ("IT", "HR", "IT", "Finance", "IT", "HR")
# Use count() to find how many times "IT" appears. Store the result in `it_count`.
# Print it.
departments = ("IT", "HR", "IT", "Finance", "IT", "HR")
print(departments.count("IT"))

# Q7. FIND INDEX
# Create: courses = ("Python", "SQL", "Power BI", "Excel")
# Use index() to find the position of "Power BI". Store the result in `powerbi_index`.
# Print it.
courses = ("Python", "SQL", "Power BI", "Excel")
print(courses.index("Power BI"))

# Q8. TUPLE WITH DIFFERENT DATA TYPES
# Create a tuple containing: - a student's name,- age,- average marks,- whether the student passed
# Print the tuple. Then print each item separately.
t = ("Radha", 26, 89)
print(t)
print(t[0],t[1],t[2])

# Q9. TUPLE VS LIST
# Create: students_list = ["Aman", "Riya", "Rahul"], students_tuple = ("Aman", "Riya", "Rahul")
# Print both. Then try to change the first item of each.
# Observe what happens. Add a comment explaining which one can be changed and which one cannot be changed.
students_list = ["Aman", "Riya", "Rahul"]
students_tuple = ("Aman", "Riya", "Rahul")
print(students_list, students_tuple )
# change wont happens in tuple but can change in list.

# Q10. MINI CHALLENGE ⭐
# Create a tuple containing the marks of 10 students.
# Your program should:
# 1. Print the tuple.
# 2. Find the number of students.
# 3. Find the highest marks.
# 4. Find the lowest marks.
# 5. Calculate the total marks.
# 6. Calculate the average marks.
# 7. Count how many students scored 80 or above.
# Store important results in variables and print them clearly.
marks = (89, 75, 83, 49, 59, 82, 95, 76, 83, 69)
# 1. Print the tuple
print("Marks:", marks)
# 2. Number of students
number_of_students = len(marks)
# 3. Highest marks
highest_marks = max(marks)
# 4. Lowest marks
lowest_marks = min(marks)
# 5. Total marks
total_marks = sum(marks)
# 6. Average marks
average_marks = total_marks / number_of_students
# 7. Students who scored 80 or above
students_80_or_above = sum(mark >= 80 for mark in marks)
print("Number of students:", number_of_students)
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)
print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("Students scoring 80 or above:", students_80_or_above)
