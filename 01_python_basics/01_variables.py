# ============================================================
# PYTHON BASICS — VARIABLES
# ============================================================


# 1. VARIABLES — SYNTAX

# Basic syntax:
# variable_name = value

# Examples:
name = "Jhon Doe"
age = 56
marks = 85.5

# A variable stores a value.
# Python automatically determines the data type of the value.
# A variable's value can be changed later.


# ============================================================
# 2. PRACTICE QUESTIONS
# ============================================================

# Q1. BASIC VARIABLE
# Create a variable called `name` and store your name in it. Print the variable.

print(name)


# Q2. MULTIPLE VARIABLES
# Create variables for:
# - name
# - age
# - city
# Print all three variables.

city = "New York"  # Replace "New York" with your city
print(name, age, city)  


# Q3. VARIABLE REASSIGNMENT
# Create:
# age = 25
# Then change its value to 26.
# Print the final value.

age = 25 
age = 26 
print(age)


# Q4. ADDITION USING VARIABLES
# Create:
# num1 = 25
# num2 = 10
# Create a variable called `total` that stores their sum.
# Print `total`.

num1 = 25
num2 = 10
total = num1 + num2
print(total)


# Q5. MODIFYING A VARIABLE
# Create:
# score = 50
# Increase the score by 25 using the existing variable.
# Print the final score.
# Expected output: 75

score = 50
score += 25 # increasing by 25
print(score)


# Q6. STUDENT INFORMATION
# Create variables for:
# - student_name
# - student_age
# - student_marks
# Give them appropriate values.
# Print all three variables.

student_name = "Alice"
student_age = 16
student_marks = 79.5
print(student_name, student_age, student_marks)


# Q7. CALCULATION USING VARIABLES
# Create:
# length = 10
# width = 5
# Create a variable called `area` that calculates
# the area of the rectangle.
# Print the area.

length = 10
width = 5
area = length * width
print(area)


# Q8. PRINT MULTIPLE VARIABLES
# Create variables for:
# - first_name
# - last_name
# - age
# Print all three in one print() statement.

first_name = "Rahul"
last_name = "Kumar"
age = 30
print("This is", first_name, last_name, " and his age is ", age,'.')


# Q9. SWAP VARIABLES
# Create:
# a = 10
# b = 20
# Swap their values so that:
# a = 20
# b = 10
# Print both variables

a = 10
b = 20
a,b = b,a # Swapping values
print("a =", a, "b =", b)


# Q10. MINI CHALLENGE ⭐
# Create variables for:
# - student_name
# - math_marks
# - science_marks
# - english_marks
# Calculate the student's total marks and store it in: `total_marks`
# Calculate the student's average marks and store it in: `average_marks`
# Print:
# - student name
# - total marks
# - average marks

student_name = "Kiran"
math_marks = 85
science_marks = 75.5
english_marks = 92
total_marks = math_marks + science_marks + english_marks
average_marks = total_marks / 3

print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
