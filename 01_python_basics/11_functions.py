# ============================================================
# PYTHON BASICS — FUNCTIONS
# ============================================================

# 1. FUNCTIONS — SYNTAX
# A function is a reusable block of code that performs a specific task.
# Basic syntax:
# def function_name():
#     statement

# Example:
# def greet():
#     print("Hello")
# greet()

# Function with a parameter:
# def greet(name):
#     print(f"Hello {name}")
# greet("Muskan")

# Function with multiple parameters:
# def add(a, b):
#     return a + b
# result = add(10, 20)
# print(result)

# 2. NOTES
# A function is created using the `def` keyword. A function is executed when it is called.
#  Parameters are variables written inside the function definition. Arguments are the actual values passed to the function.
# Example:
# def greet(name):
#     print(name)
# greet("Muskan")
# `name` is the parameter.
# `"Muskan"` is the argument.

# The return statement sends a value back from a function.
# Example:
# def add(a, b):
#     return a + b

# A returned value can be stored in a variable.
# Example:result = add(10, 20)

# A function can have a default parameter value.
# Example:
# def greet(name="Student"):
#     print(f"Hello {name}")

# Functions help:
# - Avoid repeating code
# - Organize programs
# - Make code easier to understand
# - Make code reusable

# 3. FUNCTION PARAMETERS — SYNTAX
# One parameter:
# def function_name(parameter):
#     statement

# Multiple parameters:
# def function_name(parameter1, parameter2):
#     statement

# Default parameter:
# def function_name(name="Student"):
#     statement

# 4. RETURN — SYNTAX
# def function_name():
#     return value

# Example:
# def square(number):
#     return number * number

# 5. VARIABLE SCOPE — NOTES
# A variable created inside a function is generally a local variable.
# Example:
# def test():
#     message = "Hello"
#     print(message)

# A variable created outside a function is generally a global variable.
# Example:
# name = "Muskan"
# def greet():
#     print(name)

# ============================================================
# 6. PRACTICE QUESTIONS
# ============================================================

# Q1. BASIC FUNCTION
# Create a function called `greet()`. The function should print: "Hello, Python!"
# Call the function.
def greet():
    print("Hello, Python!")

greet()

# Q2. FUNCTION WITH A PARAMETER
# Create a function called `greet_student(name)`. It should print: "Hello, <name>!"
# Call the function using your own name.
def greet_student(name):
    print(f"Hello, {name}")

greet_student("Navya")

# Q3. FUNCTION WITH TWO PARAMETERS
# Create a function called `add_numbers(a, b)`. It should calculate and print the sum of the two numbers.
# Call the function with two numbers.
def add_numbers(a, b):
    print(a + b)

add_numbers(8,9)

# Q4. RETURN A VALUE
# Create a function called `add_numbers(a, b)`. Use return to return the sum.
# Store the returned value in a variable called `result`. Print the result
def add_numbers(a, b):
    return a + b

result = add_numbers(6, 89)
print(result)

# Q5. SUBTRACTION FUNCTION
# Create a function called `subtract(a, b)`. Return the result of a - b.
# Call the function and print the result.
def subtract(a,b):
    return a - b

result = subtract(86,52)
print(result)

# Q6. MULTIPLICATION FUNCTION
# Create a function called `multiply(a, b)`. Return the multiplication result.
# Call the function with two numbers. Print the result.
def multiply(a, b):
    return a * b

result = multiply(7,9)
print(result)

# Q7. CHECK EVEN OR ODD
# Create a function called `check_even(number)`. The function should return:
# "Even" if the number is even. "Odd" if the number is odd. Call the function and print the result.
def check_even(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

check_even(89)

# Q8. PASS OR FAIL
# Create a function called `check_result(marks)`. If marks are greater than or equal to 40, return "Pass".
# Otherwise return "Fail". Call the function with different marks.
def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

print (check_result(65))

# Q9. CALCULATE AVERAGE
# Create a function called `calculate_average(a, b, c)`. Calculate the average of three numbers.
# Return the result. Store the result in a variable and print it.
def calculate_average(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg

print(calculate_average(12,34,68))    

# Q10. FIND THE LARGEST NUMBER
# Create a function called `find_largest(a, b)`. Use conditions to determine which number is larger.
# Return the larger number. Do not use max().
def find_largest(a, b):
    if a > b:
        print(f"{a} is bigger")
    else:
        print(f"{b} is bigger")

find_largest(86,79)

# Q11. DEFAULT PARAMETER
# Create a function called `greet_student(name="Student")`. If a name is provided, greet that person.
# If no name is provided, greet "Student". Call the function:1. Without an argument, 2. With a name.
def greet_student(name="Student"):
    print(f"Hello, {name}!")
greet_student()
greet_student("Navya")

# Q12. CALCULATE AREA
# Create a function called `rectangle_area(length, width)`. Calculate the area of a rectangle.
# Return the result. Call the function with different values.
def rectangle_area(length, width):
    area = length * width
    return area

print(rectangle_area(8,6))

# Q13. CALCULATE TOTAL MARKS
# Create a function called `calculate_total(math, science, english)`. Calculate and return the total marks.
# Call the function and print the result.
def calculate_total(math, science, english):
    total = math + science + english
    return total
print(calculate_total(78,96,86))

# Q14. STUDENT AVERAGE
# Create a function called `student_average(marks)`. The function should accept a list of marks.
# Calculate the average. Return the average.
# Call the function using: [75, 82, 91, 68, 88]
def student_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)
    return average
result = student_average([75, 82, 91, 68, 88])
print(result)

# Q15. COUNT PASSING STUDENTS
# Create a function called `count_passed(marks)`. The function should accept a list of marks.
# Count how many students scored 40 or above. Return the count.
#Call the function using: [35, 78, 92, 41, 29, 67]
def count_passed(marks):
    passed = 0
    for mark in marks:
        if mark >= 40:
            passed = passed + 1
    return passed
result = count_passed([35, 78, 92, 41, 29, 67])
print(result)

# Q16. FIND HIGHEST MARKS
# Create a function called `find_highest(marks)`. The function should accept a list of marks.
# Use a loop to find the highest mark. Do not use max(). Return the highest mark.
def find_highest(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest
marks = [65, 82, 91, 74, 88]
result = find_highest(marks)
print("Highest Marks:", result)

# Q17. FUNCTION WITH MULTIPLE RESULTS
# Create a function called `student_analysis(marks)`. The function should calculate:
# - total marks
# - average marks
# - highest marks
# - lowest marks
# Return all four results. Call the function and print the results.
def student_analysis(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = marks[0]
    lowest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
    return total, average, highest, lowest
marks = [75, 82, 91, 68, 88]
total, average, highest, lowest = student_analysis(marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Q18. FUNCTION WITH CONDITION
# Create a function called `scholarship_eligibility(marks, attendance)`. A student is eligible if:
# - marks >= 80
# - attendance >= 75
# Return: "Eligible" or "Not Eligible". Call the function with different values.
def scholarship_eligibility(marks, attendance):
    if marks >= 80 and attendance >= 75:
        return "Eligible"
    else:
        return "Not Eligible"
print(scholarship_eligibility(85, 80))
print(scholarship_eligibility(75, 80))
print(scholarship_eligibility(90, 70))

# Q19. FUNCTION USING A DICTIONARY
# Create a function called `student_info(student)`. The function should accept a dictionary containing:
# - name
# - age
# - marks
# Print the student's information using the dictionary. Call the function using a student dictionary.
def student_info(student):
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Marks:", student["marks"])
student = { "name": "Rahul", "age": 21, "marks": 85}
student_info(student)

# Q20. MINI CHALLENGE ⭐
# Create a function called `analyze_student(student)`. The function should accept a dictionary containing:
# name
# math
# science
# english
# attendance
# The function should:
# 1. Calculate total marks.
# 2. Calculate average marks.
# 3. Determine the grade:
#    90+ → A
#    80–89 → B
#    70–79 → C
#    60–69 → D
#    Below 60 → F
# 4. Check whether attendance is >= 75.
# 5. Determine whether the student passed.
# 6. Return the student's:
#    - name
#    - total
#    - average
#    - grade
#    - attendance status
#    - final result
# Call the function with a student dictionary.
# Print the returned results clearly.
# Q20. MINI CHALLENGE ⭐

def analyze_student(student):
    # 1. Calculate total marks
    total = student["math"] + student["science"] + student["english"]
    # 2. Calculate average marks
    average = total / 3
    # 3. Determine grade
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    # 4. Check attendance
    if student["attendance"] >= 75:
        attendance_status = "Good"
    else:
        attendance_status = "Low"
    # 5. Determine whether student passed
    if average >= 60 and student["attendance"] >= 75:
        final_result = "Passed"
    else:
        final_result = "Failed"
    # 6. Return all results
    return (
        student["name"],
        total,
        average,
        grade,
        attendance_status,
        final_result
    )
student = {
    "name": "Rahul",
    "math": 85,
    "science": 90,
    "english": 80,
    "attendance": 82
}
name, total, average, grade, attendance_status, final_result = analyze_student(student)
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
print("Attendance Status:", attendance_status)
print("Final Result:", final_result)