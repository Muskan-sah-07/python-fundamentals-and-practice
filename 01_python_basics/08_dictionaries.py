# ============================================================
# PYTHON BASICS — DICTIONARIES
# ============================================================

# 1. DICTIONARIES — SYNTAX
# A dictionary stores data in key-value pairs. Dictionaries are created using curly brackets {}.
# Syntax: dictionary_name = {"key": value}
# Example: student = {"name": "Rahul","age": 21,"marks": 85}
# Access a value using its key: dictionary_name["key"]
# Example: print(student["name"])

# 2. NOTES
# A dictionary stores data as key-value pairs.
# Example: student = {"name": "Rahul","age": 21 }
# "name" and "age" are keys. "Rahul" and 21 are values.

# Dictionaries: Store data using key-value pairs, Are changeable (mutable), 
# Keys must be unique, Values can be duplicated, Can contain different data types
# A dictionary can contain: strings, integers, floats, booleans, lists, tuples, other dictionaries.

# 3. ACCESSING VALUES — SYNTAX
# Access using a key: student["name"]
# Using get(): student.get("name")
# get() is useful because it returns None if the key does not exist instead of immediately causing a KeyError.

# 4. ADDING AND UPDATING VALUES — SYNTAX
# Add a new key-value pair: student["city"] = "Delhi"
# Update an existing value: student["age"] = 22

# 5. REMOVING ITEMS — SYNTAX

# pop(): Removes a specific key and returns its value.
# student.pop("age")
# popitem(): Removes the last inserted key-value pair.
# student.popitem()
# del: Deletes a specific key-value pair.
# del student["age"]
# clear(): Removes all items.
# student.clear()

# 6. DICTIONARY METHODS — SYNTAX

# keys(): Returns all keys.
# student.keys()
# values(): Returns all values.
# student.values()
# items(): Returns key-value pairs.
# student.items()
# update(): Adds or updates multiple key-value pairs.
# student.update({"city": "Delhi", "age": 22})
# len(): Returns the number of key-value pairs.
# len(student)

# 7. PRACTICE QUESTIONS

# Q1. CREATE A DICTIONARY
# Create a dictionary called `student` containing: name, age, department, marks.
# Give each key an appropriate value. Print the dictionary.
student = { "name":"Navya", "age":26, "department":"HR", "marks":89}
print(student)
print(type(student))

# Q2. ACCESS VALUES
# Using the student dictionary from Q1:
# Print: name, department, marks. Access the values using their keys.
student = { "name":"Navya", "age":26, "department":"HR", "marks":89}
print(student.keys())

# Q3. GET METHOD
# Create: student = {"name": "Rahul", "age": 21, "marks": 85 }
# Use get() to print the student's name and age.
student = {"name": "Rahul", "age": 21, "marks": 85 }
print(student.get("name"), student.get("age"))

# Q4. ADD A NEW VALUE
# Create: student = {"name": "Rahul", "age": 21}. Add: "city": "Delhi"
# Print the updated dictionary.
student = {"name": "Rahul", "age": 21}
student["city"] = "Delhi"
print(student)

# Q5. UPDATE A VALUE
# Create: student = { "name": "Rahul", "age": 21, "marks": 75 }
# Change the marks to 85. Print the updated dictionary.
student = { "name": "Rahul", "age": 21, "marks": 75 }
student["marks"] = 85
print(student)

# Q6. ADD MULTIPLE VALUES
# Create: student = {"name": "Rahul", "age": 21}. Use update() to add: department, marks, city.
# Print the updated dictionary.
student = {"name": "Rahul", "age": 21}
student.update({"department": "HR", "marks": 69, "city": "NY"})
print(student)


# Q7. REMOVE USING POP()
# Create: student = { "name": "Rahul", "age": 21, "marks": 85, "city": "Delhi" }
# Remove the "city" key using pop(). Store the removed value in `removed_city`.
# Print the removed value and updated dictionary.
student = { "name": "Rahul", "age": 21, "marks": 85, "city": "Delhi" }
removed_city = student.pop("city")
print(removed_city)
print(student)

# Q8. DELETE USING DEL
# Create: student = { "name": "Rahul", "age": 21, "marks": 85 }
# Delete the "age" key using del. Print the updated dictionary.
student = { "name": "Rahul", "age": 21, "marks": 85 } 
del student["age"]
print(student)

# Q9. DICTIONARY LENGTH
# Create a dictionary containing information about a student.
# Use len() to find the number of key-value pairs. Store the result in `dictionary_length`. Print it.
student = { "name": "Rahul", "age": 21, "marks": 85, "city": "Delhi" }
dictionary_length = len(student)
print(dictionary_length)

# Q10. KEYS
# Create: student = { "name": "Rahul", "age": 21, "marks": 85, "department": "Computer Science" }
# Use keys() to print all the keys.
student = { "name": "Rahul", "age": 21, "marks": 85, "department": "Computer Science" }
print(student.keys())

# Q11. VALUES
# Using the same student dictionary: Use values() to print all the values.
student = { "name": "Rahul", "age": 21, "marks": 85, "department": "Computer Science" }
print(student.values())

# Q12. ITEMS
# Using the same student dictionary: Use items() to print all key-value pairs.
student = { "name": "Rahul", "age": 21, "marks": 85, "department": "Computer Science" }
print(student.items())

# Q13. CHECK WHETHER A KEY EXISTS
# Create: student = { "name": "Rahul", "age": 21, "marks": 85 }
# Check whether: "name" exists in the dictionary, "city" exists in the dictionary.
# Print both results.
student = { "name": "Rahul", "age": 21, "marks": 85 }
print(student.get("name"))  # Rahul
print(student.get("city"))  # None

# Q14. STUDENT PROFILE
# Create a dictionary containing: name, age, gender, department, year, marks.
# Print each value individually using its key.
student = { "name": "Rahul", "age": 21, "marks": 85, "department": "Computer Science", "gender": "Male", "year": 2021 }
print(student.get("name"))
print(student.get("age"))
print(student.get("gender"))
print(student.get("department"))
print(student.get("year"))
print(student.get("marks"))

# Q15. CALCULATE FROM DICTIONARY
# Create: student = { "name": "Rahul",  "math": 85, "science": 78, "english": 92 }
# Calculate: total marks, average marks. Store them in: total_marks average_marks.
# Print both results.
student = { "name": "Rahul",  "math": 85, "science": 78, "english": 92 }
total_marks = student.get("math") + student.get("science") + student.get("english")
average_marks = total_marks / 3
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

# Q16. NESTED LIST INSIDE DICTIONARY
# Create a dictionary: student = { "name": "Rahul", "courses": ["Python", "SQL", "Power BI"] }
# Print: student name, first course, last course
# Access the course values through the dictionary.
student = { "name": "Rahul", "courses": ["Python", "SQL", "Power BI"] }
print(student.get("name"))
print(student.get("courses")[0])
print(student.get("courses")[-1])
print(student.keys())

# Q17. DICTIONARY OF STUDENTS
# Create a dictionary containing three students. Each student should have: name, age, marks
# Print the complete dictionary.
# Then access and print the information of one student.
student = {
    "student1": {"name": "Rahul", "age": 21, "marks": 85},
    "student2": {"name": "Rakul", "age": 26, "marks": 90},
    "student3": {"name": "Riya", "age": 28, "marks": 69}
}
# Print complete dictionary
print(student)
# Access and print information of one student
print(student["student1"])
# Print individual information
print(student["student1"]["name"])
print(student["student1"]["age"])
print(student["student1"]["marks"])

# Q18. STUDENT ANALYSIS
# Create a dictionary: student = { "name": "Priya", "math": 85,  "science": 92,  "english": 78, "attendance": 88 }
# Calculate: total marks, average marks. Then check whether attendance is greater than or equal to 75.
# Print all results clearly.
student = { "name": "Priya", "math": 85,  "science": 92,  "english": 78, "attendance": 88 }
total_marks = ( student.get("math") + student.get("science") + student.get("english"))
average_marks = total_marks/ 3
attendance_check = ( student.get("attendance") >= 75)
print(total_marks)
print(average_marks)
print(attendance_check)

# Q19. UPDATE STUDENT RECORD
# Create:student = { "name": "Aman", "age": 20, "department": "IT", "marks": 72}
# Perform the following:
# 1. Change marks to 82.
# 2. Add city = "Mumbai".
# 3. Add attendance = 90.
# 4. Remove age.
# 5. Print all keys.
# 6. Print all values.
# Print the final dictionary.
student = {
    "name": "Aman",
    "age": 20,
    "department": "IT",
    "marks": 72
}
# 1. Change marks to 82
student["marks"] = 82
# 2. Add city = "Mumbai"
# 3. Add attendance = 90
student.update({
    "city": "Mumbai",
    "attendance": 90
})
# 4. Remove age
del student["age"]
# 5. Print all keys
print(student.keys())
# 6. Print all values
print(student.values())
# Print the final dictionary
print(student)

# Q20. MINI CHALLENGE ⭐
# Create a dictionary containing information for 5 students.
# Each student should have: name, department, marks, attendance
# Your program should:
# 1. Store all five student records.
# 2. Print all student records.
# 3. Access one student's information.
# 4. Find the student with the highest marks.
# 5. Find the student with the lowest marks.
# 6. Calculate the average marks.
# 7. Check which students have attendance >= 75.
# Store important results in variables and print them clearly.
students = {
    "student1": {
        "name": "Rahul",
        "department": "IT",
        "marks": 85,
        "attendance": 90
    },
    "student2": {
        "name": "Riya",
        "department": "CSE",
        "marks": 92,
        "attendance": 88
    },
    "student3": {
        "name": "Aman",
        "department": "ECE",
        "marks": 76,
        "attendance": 72
    },
    "student4": {
        "name": "Priya",
        "department": "IT",
        "marks": 68,
        "attendance": 80
    },
    "student5": {
        "name": "Neha",
        "department": "CSE",
        "marks": 95,
        "attendance": 70
    }
}
# 1. Store all five student records
# Already stored in the students dictionary
# 2. Print all student records
print("All Student Records:")
print(students)
# 3. Access one student's information
one_student = students["student1"]
print("\nOne Student's Information:")
print(one_student)
# 4. Find the student with the highest marks
highest_student = max(students.values(), key=lambda student: student["marks"])
# 5. Find the student with the lowest marks
lowest_student = min(students.values(), key=lambda student: student["marks"])
# 6. Calculate the average marks
total_marks = sum(student["marks"] for student in students.values())
average_marks = total_marks / len(students)
# 7. Check which students have attendance >= 75
students_with_good_attendance = []
for student in students.values():
    if student["attendance"] >= 75:
        students_with_good_attendance.append(student["name"])
# Print important results clearly
print("\nStudent with Highest Marks:")
print(highest_student)
print("\nStudent with Lowest Marks:")
print(lowest_student)
print("\nAverage Marks:")
print(average_marks)
print("\nStudents with Attendance >= 75:")
print(students_with_good_attendance)