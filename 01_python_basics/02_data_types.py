# ============================================================
# PYTHON BASICS — DATA TYPES
# ============================================================


#SYNTAX:
# Python has different data types for storing different kinds of values.
# Integer: age = 26
# Float: marks = 85.5
# String: name = "John Doe"
# Boolean: is_student = True
# Check the data type: print(type(age)), print(type(marks))


# 2. NOTES

# Common Python data types:
# int : Used for whole numbers. Example: age = 26
# float: Used for numbers containing decimal values. Example: marks = 85.5
# str: Used for text. Example: name = "John Doe"
# bool: Used for True or False values. Example: is_student = True

# Python automatically determines the data type based on the value assigned to the variable.
#The type() function is used to check the data type of a value or variable.
# Example: number = 100
# print(type(number))


# 3. TYPE CONVERSION — SYNTAX

# Convert to integer: int(value)
# Convert to float: float(value)
# Convert to string: str(value)
# Convert to boolean: bool(value)

# Examples: number = "100"
# converted_number = int(number)


# 4. BUILT-IN FUNCTIONS — NOTES

# Some useful built-in functions: type() # Checks the data type.
# int(): Converts a value to an integer.
# float(): Converts a value to a float.
# str(): Converts a value to a string.
# bool(): Converts a value to a Boolean.
# len(): Returns the number of items/characters.
# round(): Rounds a number.
# abs(): Returns the absolute value.
# max(): Returns the largest value.
# min(): Returns the smallest value.
# sum(): Returns the total of numeric values.


# 5. PRACTICE QUESTIONS

# Q1. INTEGER
# Create a variable called `age` and store your age as an integer.
# Print the variable and its data type using type().
age = 16
print(age)
print(type(age))

# Q2. FLOAT
# Create a variable called `height` and store a decimal value.
# Print the variable and its data type.
height = 5.5
print(height)
print(type(height))

# Q3. STRING
# Create a variable called `course_name` and store: "Data Analytics"
# Print the variable and its data type.
course_name = 'Data Analyst'
print(type(course_name))
print(course_name)

# Q4. BOOLEAN
# Create a variable called `is_learning_python` and store a Boolean value.
# Print the variable and its data type.
is_learning_python = True
print(is_learning_python)
print(type(is_learning_python))

# Q5. IDENTIFY DATA TYPES
# Create the following variables: number = 100, price = 99.99, name = "Muskan", completed = True
# Print the data type of each variable using type().
number = 100
price = 99.99
name = 'Muskan'
completed = True
print(type(number))
print(type(price))
print(type(name))
print(type(completed))

# Q6. STRING TO INTEGER
# Create: number = "500"
# Convert the string into an integer. Store the result in a new variable called `converted_number`.
# Print the value and its data type.
number = '500'
converted_number = int(number)
print(converted_number)
print(type(converted_number))

# Q7. STRING TO FLOAT
# Create: price = "149.99". Convert the string into a float. Store the result in `converted_price`.
# Print the value and its data type.
price = '149.99'
converted_price = float(price)
print(converted_price)
print(type(converted_price))

# Q8. INTEGER TO STRING
# Create: age = 26. Convert the integer into a string. Store it in `age_text`.
# Print the value and its data type.
age = 26
age_txt = str(age)
print(age_txt)
print(type(age_txt))

# Q9. CALCULATE AFTER TYPE CONVERSION
# Create: marks1 = "80", marks2 = "90". Convert both values into integers.
# Calculate their total. Store the result in `total_marks`. Print the total.
marks1 = '80'
marks2 = '90'
converted1 = int(marks1)
converted2 = int(marks2)
total_marks = converted1 + converted2
print(total_marks)

# Q10. LENGTH OF A STRING
# Create a variable: text = "Python Programming". Use len() to find the number of characters in the string.
# Store the result in a variable called `length`. Print the result.
text = "Python Programming"
lenght = len(text)
print(lenght)

# Q11. ROUND A NUMBER
# Create: number = 85.6789. Use round() to round the number to 2 decimal places.
# Store the result in `rounded_number`. Print the result.
number = 85.6789
rounded_number = round(number,2)
print(rounded_number)

# Q12. MAXIMUM AND MINIMUM
# Create three variables: marks1 = 75, marks2 = 88, marks3 = 92
# Use max() to find the highest marks. Use min() to find the lowest marks. Print both results.
marks1 = 75
marks2 = 88
marks3 = 92
highest_marks = max(marks1,marks2,marks3)
lowest_marks = min(marks1,marks2,marks3)
print(highest_marks)
print(lowest_marks)

# Q13. SUM AND AVERAGE
# Create a list of five marks. Use sum() to calculate the total marks.
# Calculate the average marks. Print the total and average.
m1 = 75
m2 = 88 
m3 = 92
m4 = 85 
m5 = 90
total_marks = sum([m1,m2,m3,m4,m5])
print(total_marks)
average_marks = total_marks / 5
print(average_marks)

# Q14. MIXED DATA TYPES
# Create variables for a student: student_name → string, age → integer, average_marks → float, passed → Boolean.
# Print each variable and its data type. Make sure each variable uses the correct data type.
student_name = "Rakul"
age = 26
average_marks = 78.93
passed = True

print(student_name)
print(type(student_name))
print(age)
print(type(age))
print(average_marks)
print(type(average_marks))
print(passed)
print(type(passed))

# Q15. MINI CHALLENGE ⭐
# You receive student information as strings: student_name = "Rahul", age = "21", math_marks = "85", science_marks = "78.5".
# Your task:
# 1. Convert age into an integer.
# 2. Convert math_marks into an integer.
# 3. Convert science_marks into a float.
# 4. Calculate total marks.
# 5. Calculate average marks.
# 6. Print the student's name.
# 7. Print the converted values.
# 8. Print the total marks.
# 9. Print the average marks.
# 10. Print the data type of age, math_marks and science_marks.
student_name = "Rahul"
age = "21"
math_marks = "85"
science_marks = "78.5"
age = int(age)  #1
math_marks = int(math_marks)  #2
science_marks = float(science_marks)  #3
total_marks = math_marks + science_marks  #4
average_marks = total_marks / 2  #5
print(student_name)  #6
print(age)  #7
print(math_marks)
print(science_marks)
print(total_marks)  #8
print(average_marks)  #9
print(type(age))  #10
print(type(math_marks)) #11
print(type(science_marks))  #12