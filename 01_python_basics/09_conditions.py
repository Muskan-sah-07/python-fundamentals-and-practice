# ============================================================
# PYTHON BASICS — CONDITIONS
# ============================================================

# 1. CONDITIONS — SYNTAX
# Basic if statement:
# if condition:
#     statement
# Example:
# age = 20
# if age >= 18:
#     print("Adult")

# if-else:
# if condition:
#     statement_if_true
# else:
#     statement_if_false
# Example:
# age = 16
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# if-elif-else:
# if condition1:
#     statement
# elif condition2:
#     statement
# else:
#     statement
# Example:
# marks = 75
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# else:
#     print("C")

# 2. NOTES
# Conditions allow a program to make decisions.
# A condition normally produces: True or False
# Comparison operators can be used in conditions:
# ==
# !=
# >
# <
# >=
# <=

# Logical operators can combine conditions: and or not

# Python uses indentation to identify which statements belong to a condition.
# Example:
# if marks >= 40:
#     print("Pass")
# The print statement must be indented.

# 3. NESTED CONDITIONS — SYNTAX
# A condition inside another condition is called a nested condition.
# Example:
# age = 20
# has_id = True
# if age >= 18:
#     if has_id:
#         print("Entry allowed")

# 4. PRACTICE QUESTIONS

# Q1. BASIC IF
# Create: age = 20
# Check whether the age is greater than or equal to 18. If it is, print: "Adult"
age = 20 
if age >= 18:
    print("Adult")


# Q2. IF-ELSE
# Create: age = 16
# If age is greater than or equal to 18, print: "Adult". Otherwise print:"Minor"
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Q3. CHECK MARKS
# Create: marks = 75
# If marks are greater than or equal to 40: print "Pass", Otherwise: print "Fail"
marks = 75
if marks >= 40:
    print("Pass")
else:
    print("Fail")    

# Q4. POSITIVE OR NEGATIVE
# Create: number = -10
# Check whether the number is positive or negative. Print the appropriate message.
number = -10
if number > 0:
    print("Number is Positive")
else:
    print("Number is negative")    

# Q5. EVEN OR ODD
# Create: number = 25
# Check whether the number is even or odd. Print the appropriate message.
number = 25
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Q6. IF-ELIF-ELSE
# Create: marks = 85
# Use the following grading system:
# 90 or above → "A"
# 80 to 89   → "B"
# 70 to 79   → "C"
# 60 to 69   → "D"
# Below 60   → "F"
# Print the grade.
marks = 85
if marks >= 90:
    print(" Your grade is A")
elif marks >= 80 and marks <= 89:
    print(" Your grade is B")
elif marks >= 70 and marks <= 79:
    print(" Your grade is C")
elif marks >= 60 and marks <= 69:
    print(" Your grade is D")
else:
    print(" Your grade is F")    

# Q7. AGE CATEGORY
# Create: age = 25
# Classify the person as:
# Below 13  → "Child"
# 13–19     → "Teenager"
# 20–59     → "Adult"
# 60+       → "Senior"
# Print the category.
age = 25
if age < 13:
    print("Person is a Child")
elif age  >= 13 and age <= 19:
    print("Person is a Teenager")
elif age  >= 20 and age <= 59:
    print("Person is a Adult")    
else:
    print("Person is a Senior")

# Q8. LARGEST OF TWO NUMBERS
# Create: a = 45, b = 72
# Use conditions to find which number is larger. Print the larger number.
a = 45
b = 72
if a > b:
    print(f"{a} is greater.")
else:
    print(f"{b} is greater.")

# Q9. EQUAL OR NOT
# Create: a = 50, b = 50
# Check whether the two numbers are equal. Print an appropriate message.
a = 50
b = 50
if a == b:
    print(" both numbers are equal")
else:
    print(" both number are not equal.")

# Q10. PASS WITH ATTENDANCE
# Create: marks = 65, attendance = 80
# A student passes only if: marks >= 40 and attendance >= 75
# Check both conditions and print: "Pass" or "Fail"
marks = 65
attendance = 80
if marks >= 40 and attendance >= 75:
    print(" You Pass")
else:
    print(" You Fail")

# Q11. ELIGIBILITY CHECK
# Create: age = 22, has_degree = True
# A person is eligible if: age >= 18 and has_degree is True
# Print whether the person is eligible.
age = 22
has_degree = True
if age >= 18 and has_degree is True:
    print(" Person is eligible.")
else:
    print(" Person is not eligible.")
    
# Q12. MULTIPLE CONDITIONS
# Create: marks = 85, attendance = 90, fees_paid = True
# A student can appear for an exam only if: marks >= 40, attendance >= 75, fees_paid is True
# Print: "Allowed" or "Not Allowed"
marks = 85
attendance = 90
fees_paid = True
if marks >= 40 and attendance >= 75 and fees_paid is True:
    print(" You are allowed to appear in a paper.")
else:
    print(" You are not allowed to appear in a paper.")

# Q13. TEMPERATURE
# Create: temperature = 35
# Classify the temperature:
# Below 10      → "Cold"
# 10–24         → "Cool"
# 25–34         → "Warm"
# 35 or above   → "Hot"
# Print the result.
temperature = 35
if temperature < 10:
    print(" You have Cold")
elif temperature >= 10 and temperature <= 24:
    print(" You have Cool")
elif temperature >= 25 and temperature <= 34:
    print(" You have Warm") 
else:
    print(" You have Hot.")
    
# Q14. SCHOLARSHIP
# Create: marks = 88, attendance = 90
# A student qualifies for a scholarship if: marks >= 85 AND attendance >= 80
# Print whether the student qualifies.
marks = 88
attendance = 90
if marks >= 85 and attendance >= 80:
    print(" You Qualified")
else:
    print(" Sorry!, Try Again. You Didnt Qualified.")


# Q15. LOGIN CHECK
# Create: username = "admin", password = "12345"
# Check: username must be "admin", password must be "12345"
# If both are correct, print: "Login successful", Otherwise print: "Invalid username or password"
username = "admin"
password = "12345"
if username is "admin" and password is "12345":
    print("Login successful")
else:
    print("Invalid username or password")
    
    
# Q16. NESTED CONDITION
# Create: age = 22, has_id = True
# First check whether the person is 18 or older.
# If they are: check whether they have an ID.
# Print: "Entry allowed". if both conditions are satisfied.
age = 22
has_id = True
if age >= 18 and has_id is True:
    print(" Entry allowed")
else:
    print(" Entry not allowed.")

# Q17. STUDENT RESULT
# Create: math = 75, science = 82, english = 68
# Calculate the average marks.
# Classify the result:
# 90+ → "Excellent"
# 75–89 → "Very Good"
# 60–74 → "Good"
# 40–59 → "Pass"
# Below 40 → "Fail"
# Print the average and result.
math = 75
science = 82
english = 68
total_marks = math + science + english
average_marks = total_marks / 3
print(average_marks)
if average_marks >= 90:
    print(" Excellent")
elif average_marks >= 75 and average_marks <= 89:
    print(" Very Good")
elif average_marks >= 60 and average_marks <= 74:
    print("Good")
elif average_marks >= 40 and average_marks <= 59:
    print(" Pass ")
else:
    print("Fail")
    
# Q18. NUMBER CLASSIFICATION
# Create: number = 0
# Check whether the number is: Positive, Negative, or Zero
# Print the appropriate result.
number = 0
if number == 0:
    print("Zero")
elif number > 0:
    print(" Positive")
else:
    print(" Negative")

# Q19. STUDENT ELIGIBILITY
# Create: marks = 82, attendance = 78, age = 20
# A student is eligible if:
# - marks >= 75
# - attendance >= 75
# - age >= 18
# If eligible, print: "Student is eligible"  Otherwise print: "Student is not eligible"
# Also print which condition failed if the student is not eligible.
marks = 82
attendance = 78
age = 20
if  marks >= 75 and attendance >= 75 and age >= 18:
    print("Student is eligible")
else:
    print("Student is not eligible")
    
    
# Q20. MINI CHALLENGE ⭐
# Create: student_name = "Rahul", math_marks = 85, science_marks = 78, english_marks = 92, attendance = 88
# Your program should:
# 1. Calculate total marks.
# 2. Calculate average marks.
# 3. Check whether the student passed.
# 4. Check whether attendance is sufficient.
# 5. Assign a grade:
#    90+ → A
#    80–89 → B
#    70–79 → C
#    60–69 → D
#    Below 60 → F
# 6. Print the student's name.
# 7. Print total marks.
# 8. Print average marks.
# 9. Print attendance.
# 10. Print the grade.
# 11. Print the final result.
student_name = "Rahul"
math_marks = 85
science_marks = 78
english_marks = 92
attendance = 88
total_marks = math_marks + science_marks + english_marks
average_marks = total_marks / 3
print(total_marks)
print(average_marks)
print( attendance)
print(student_name)
if average_marks >= 90:
    print("A")
elif average_marks <= 89 and average_marks >= 80:
    print("B")
elif average_marks <= 79 and average_marks >= 70:
    print("C")  
elif average_marks <= 69 and average_marks >= 60:
    print("D")
else:
    print("F")
print(f" {student_name} has a total marks of {total_marks} with the attendance of {attendance}")
    