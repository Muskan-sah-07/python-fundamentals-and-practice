# ============================================================
# PYTHON BASICS — LISTS
# ============================================================

# 1. LISTS — SYNTAX- A list is an ordered collection of items. Lists are created using square brackets [].
# Example: students = ["Aman", "Riya", "Rahul", "Priya"]

# A list can contain different data types: mixed_list = ["Muskan", 26, 85.5, True]
# Access an item using its index: list[index]
# Example: print(students[0])

# Negative indexing: print(students[-1])

# Slicing: list[start:end]
# Example: print(students[0:2])


# 2. NOTES

# Lists are:# - Ordered, changeable (mutable), allow duplicate values, and can contain different data types.
# Python uses zero-based indexing. The first item has index 0.
# Example: students = ["Aman", "Riya", "Rahul"]
# Aman  -> index 0, Riya  -> index 1, Rahul -> index 2

# Lists can be changed after they are created.
# Example: students[0] = "Arjun"

# The len() function returns the number of items in a list.
# Example: len(students)


# 3. LIST METHODS — SYNTAX
# append()- Adds one item to the end of a list.
# list.append(item)
# insert()- Adds an item at a specific position.
# list.insert(index, item)
# remove()  Removes a specific item.
# list.remove(item)
# pop()- Removes an item using its index.
# list.pop(index)
# sort()- Sorts a list.
# list.sort()
# reverse()- Reverses the order of a list.
# list.reverse()
# extend()- Adds multiple items to a list.
# list.extend(another_list)
# count()- Counts how many times an item appears.
# list.count(item)
# index() - Finds the position of an item.
# list.index(item)


# 4. PRACTICE QUESTIONS

# Q1. CREATE A LIST
# Create a list called `students` containing five student names.
# Print the list.
student = ["Ram","Shyam","Jesus","Kirti","Radha"]
print(student)

# Q2. ACCESS LIST ITEMS
# Create: students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
# Print:  the first student, the third student, and the last student using indexing.
students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
print(students[0], students[2], students[-1])

# Q3. NEGATIVE INDEXING
# Create a list of five course names. Use negative indexing to print:the last course, the second-last course
course = ["Economy","Sql","AI","Math","Statistics"]
print(course[-1], course[-2])

# Q4. LIST LENGTH
# Create a list containing six student names. Use len() to find the number of students.
# Store the result in `student_count`. Print it.
student = ["Ram","Shyam","Jesus","Kirti","Radha","Bini"]
student_count = len(student)
print(student_count)

# Q5. CHANGE A LIST ITEM
# Create: students = ["Aman", "Riya", "Rahul"]. Change "Riya" to "Priya".
# Print the updated list.
students = ["Aman", "Riya", "Rahul"]    
students[1] = "Priya"
print(students) 

# Q6. APPEND
# Create: courses = ["Python", "SQL", "Excel"]. Add "Power BI" to the end of the list using append().
# Print the updated list.
courses = ["Python", "SQL", "Excel"]
courses.append("Power BI")
print(courses)


# Q7. INSERT
# Create: students = ["Aman", "Rahul", "Priya"]. Insert "Riya" between "Aman" and "Rahul".
# Print the updated list.
students = ["Aman", "Rahul", "Priya"]
students.insert(1,"Riya")
print(students)

# Q8. REMOVE
# Create: courses = ["Python", "SQL", "Excel", "Power BI"]. Remove "Excel" using remove().
# Print the updated list.
courses = ["Python", "SQL", "Excel", "Power BI"]
courses.remove("Excel")
print(courses)

# Q9. POP
# Create: students = ["Aman", "Riya", "Rahul", "Priya"]
# Remove the last student using pop(). Store the removed student in a variable called `removed_student`.
# Print both the removed student and the updated list.
students = ["Aman", "Riya", "Rahul", "Priya"]
students.pop(-1)
print(students)

# Q10. EXTEND
# Create: technical_skills = ["Python", "SQL"] additional_skills = ["Power BI", "Excel", "Statistics"]
# Use extend() to add additional_skills to technical_skills. Print the updated list.
technical_skills = ["Python", "SQL"]
additional_skills = ["Power BI", "Excel", "Statistics"]
updated_list = technical_skills.extend(additional_skills)
print(technical_skills)

# Q11. SORT A LIST
# Create: marks = [78, 92, 65, 88, 71]. Sort the list in ascending order.
# Print the sorted list.
marks = [78, 92, 65, 88, 71]
sorted_list = marks.sort()
print(marks)

# Q12. SORT IN DESCENDING ORDER
# Create: marks = [78, 92, 65, 88, 71]. Sort the list in descending order.
# Print the result.
marks = [78, 92, 65, 88, 71]
marks.sort(reverse=True)
print(marks)

# Q13. REVERSE A LIST
# Create: students = ["Aman", "Riya", "Rahul", "Priya"]. Reverse the list using reverse().
# Print the result.
students = ["Aman", "Riya", "Rahul", "Priya"]
students.reverse()
print(students)

# Q14. COUNT ITEMS
# Create: departments = ["IT", "HR", "IT", "Finance", "IT", "HR"]. Use count() to find how many times "IT" appears.
# Store the result in `it_count`. Print it.
departments = ["IT", "HR", "IT", "Finance", "IT", "HR"]
it_count = departments.count("IT")
print(it_count)

# Q15. FIND INDEX
# Create: courses = ["Python", "SQL", "Power BI", "Excel"]. Use index() to find the position of "Power BI".
# Store the result in `powerbi_index`. Print it.
courses = ["Python", "SQL", "Power BI", "Excel"]
print(courses.index("Power BI"))

# Q16. LIST SLICING
# Create: numbers = [10, 20, 30, 40, 50, 60]
# Use slicing to print: the first three numbers, the last three numbers, numbers from index 1 to 4
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0:3], numbers[-3::], numbers[1:5])

# Q17. LIST CALCULATIONS
# Create: marks = [75, 82, 91, 68, 88]
# Use: sum(), len(), max(), min()
# Find:total marks, average marks, highest marks, lowest marks
# Store the results in variables and print them.
marks = [75, 82, 91, 68, 88]
total_marks = sum(marks)
l = len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = total_marks / l
print(total_marks, average_marks, lowest_marks, highest_marks)

# Q18. STUDENT LIST
# Create a list containing five student names.
# Perform the following:1. Add one student, 2. Remove one student, 3. Sort the list alphabetically.
# 4. Print the first student, 5. Print the last student, 6. Print the total number of students.
students = ["Aman", "Riya", "Rahul", "Priya","Rishi"]
students.append("Ritik")
students.pop(2)
students.sort()
print(students[0], students[-1], len(students))
print(students)

# Q19. LIST ANALYSIS
# Create: marks = [45, 78, 92, 35, 88, 67, 95]
# Perform the following:1. Find the highest mark, 2. Find the lowest mark, 3. Find the total marks.
# 4. Find the number of students, 5. Calculate the average marks, 6. Sort the marks in descending order.
# Print all results.
marks = [45, 78, 92, 35, 88, 67, 95]
highest_marks = max(marks)
lowest_marks = min(marks)
total_marks = sum(marks)
l = len(marks)
average_marks = total_marks / l
sorting_marks = sorted(marks, reverse=True)
print(highest_marks, lowest_marks, total_marks, l, average_marks, sorting_marks)

# Q20. MINI CHALLENGE ⭐
# Create a list containing the marks of 10 students.
# Your program should: 1. Print the original list, 2. Find the highest marks, 3. Find the lowest marks.
# 4. Calculate the total marks, 5. Calculate the average marks, 6. Sort the marks from lowest to highest.
# 7. Sort the marks from highest to lowest, 8. Count how many students scored 80 or above.
# Store important results in variables and print them clearly.
marks = [89,75,83,49,59,82,95,76,83,69]
print(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
total_marks = sum(marks)
l = len(marks)
average_marks = total_marks / l
sorting_marks = sorted(marks)
sorting_marks1 = sorted(marks, reverse=True)
print(highest_marks, lowest_marks, total_marks, l, average_marks, sorting_marks, sorting_marks1)

