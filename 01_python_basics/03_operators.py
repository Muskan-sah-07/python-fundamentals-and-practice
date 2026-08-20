# ============================================================
# PYTHON BASICS — OPERATORS
# ============================================================

# 1. OPERATORS — SYNTAX
# Arithmetic operators:
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor division
# %   Modulus (remainder)
# **  Exponentiation
# Examples: a + b, a - b, a * b, a / b, a // b, a % b, a ** b

# Comparison operators:
# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# Examples: a == b, a != b, a > b, a < b, a >= b, a <= b

# Logical operators:
# and
# or
# not
# Examples: condition1 and condition2, condition1 or condition2, not condition

# Assignment operators:
# =   Assign
# +=  Add and assign
# -=  Subtract and assign
# *=  Multiply and assign
# /=  Divide and assign
# //= Floor divide and assign
# %=  Modulus and assign
# **= Exponent and assign

# 2. NOTES
# Operators are symbols or keywords used to perform calculations, comparisons, assignments, and logical operations.
# Arithmetic operators work with numbers. Comparison operators return a Boolean value: True or False.
# Logical operators combine or modify conditions. Assignment operators are used to assign or update values.
# The % operator returns the remainder after division. The // operator performs floor division.
# The ** operator calculates a power.

# 3. PRACTICE QUESTIONS

# Q1. ADDITION
# Create two variables: num1 = 25, num2 = 15
# Use the addition operator to calculate their sum. Store the result in `result`. Print the result.
num1 = 25
num2 = 15
result = num1 + num2
print(result)

# Q2. BASIC ARITHMETIC
# Create: a = 20, b = 5
# Calculate and print: addition, subtraction, multiplication, division
a = 20
b = 5
addition = a + b
substraction = a - b
multiplication = a * b
division = a / b
print(addition)
print(substraction)
print(multiplication)
print(division)

# Q3. FLOOR DIVISION
# Create: number = 17, divisor = 5. Use the floor division operator to find the result.
# Store it in `result`. Print the result.
num = 17
divisor = 5
result = num //divisor
print(result)

# Q4. MODULUS
# Create: number = 17, divisor = 5. Use the modulus operator to find the remainder.
# Store it in `remainder`. Print the result.
num = 17
divisor = 5
remainder = num % divisor
print(remainder)

# Q5. EXPONENTIATION
# Create: base = 2, exponent = 5
# Calculate 2 raised to the power of 5. Store the result in `result`. Print the result.
base = 2
exponent = 5
result = base ** exponent
print(result)

# Q6. COMPARISON OPERATORS
# Create: a = 25, b = 20. Use comparison operators to check: Is a greater than b?, Is a less than b?, Is a equal to b?, Is a not equal to b?
# Print each result.
a = 25
b = 20
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

# Q7. GREATER THAN OR EQUAL TO
# Create: marks = 75. Check whether the marks are greater than or equal to 40.
# Store the result in `passed`. Print the result.
marks = 75
passed = marks >= 40
print('you passed:', passed)

# Q8. LESS THAN OR EQUAL TO
# Create: age = 17. Check whether the age is less than or equal to 18.
# Store the result in `is_eligible`. Print the result.
age = 17
is_eligible = age <= 18
print('is eligible:', is_eligible)

# Q9. AND OPERATOR
# Create: age = 25, has_id = True.  Check whether: - age is greater than or equal to 18 AND has_id is True
# Store the result in `can_enter`. Print the result.
age = 25
has_id = True
can_enter = age >= 18 and has_id
print('can enter:', can_enter)

# Q10. OR OPERATOR
# Create: has_degree = True has_experience = False. Check whether the person has a degree OR experience.
# Store the result in `eligible`. Print the result.
has_degree = True
has_experience = False  
eligible = has_degree or has_experience
print('eligible:', eligible)

# Q11. NOT OPERATOR
# Create: is_absent = False. Use the `not` operator to check whether the student is NOT absent.
# Store the result in `is_present`. Print the result.
# Your Answer:
is_absent = False
is_present = not is_absent
print('is present:', is_present)

# Q12. ASSIGNMENT OPERATORS
# Create: score = 50. Use `+=` to increase the score by 20. Then use `-=` to decrease it by 10.
# Print the final score.
# Your Answer:
score = 50
score += 20
score -= 10
print('final score:', score)

# Q13. COMBINE OPERATORS
# Create: marks = 80, attendance = 85. Check whether: attendance = 85.
# Check whether:- marks are greater than or equal to 40 AND attendance is greater than or equal to 75.
# Store the result in `eligible`. Print the result.
marks = 80
attendance = 85
print(attendance)
eligible = (marks >= 40) and (attendance >= 75)   # And x , and Y
print(eligible)

# Q14. STUDENT RESULT
# Create: math_marks = 75, science_marks = 82, english_marks = 68.
# Calculate: total marks, average marks. Then check whether the average marks are greater than or equal to 40.
# Store the result in `passed`. Print the total, average, and passed status.
math_marks = 75
science_marks = 82
english_marks = 68
total_marks = math_marks + science_marks + english_marks
print(total_marks)
average_marks = (math_marks + science_marks + english_marks)/3
print(average_marks)
passed = average_marks >= 40
print(passed)

# Q15. MINI CHALLENGE ⭐
# A student wants to know whether they are eligible for a scholarship.
# Create: marks = 85, attendance = 90, family_income = 450000. 
# The student is eligible if: marks are greater than or equal to 80 AND attendance is greater than or equal to 75 AND family_income is less than or equal to 500000.
# Create a Boolean variable called `scholarship_eligible`. Print the result. Also print a clear message showing whether the student is eligible.
marks = 85 
attendance = 90
family_income = 450000
scholarship_eligible = marks >=80 and attendance >= 75 and family_income <= 500000
print('For Scholarship the student is eligible: ',scholarship_eligible)
