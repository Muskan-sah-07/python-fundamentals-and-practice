# ============================================================
# PYTHON BASICS — LOOPS
# ============================================================

# 1. LOOPS — SYNTAX
# A loop is used to repeat a block of code.
# FOR LOOP
# Basic syntax:
# for variable in sequence:
#     statement
# Example:
# for number in range(1, 6):
#     print(number)

# WHILE LOOP
# Basic syntax:
# while condition:
#     statement
# Example:
# number = 1
# while number <= 5:
#     print(number)
#     number += 1

# 2. NOTES
# A for loop is commonly used when we want to iterate through a sequence or a known range of values.
# Example: students = ["Aman", "Riya", "Rahul"]
# for student in students:
#     print(student)

# range() generates a sequence of numbers.
# range(stop)
# range(start, stop)
# range(start, stop, step)
# Example: range(5)    # gives numbers from 0 to 4.
# Example: range(1, 6) # gives numbers from 1 to 5.

# A while loop continues running as long as its condition is True.
# Make sure the condition eventually becomes False, otherwise the loop can become infinite.

# break- Stops the loop immediately.
# Example:
# for number in range(1, 10):
#     if number == 5:
#         break
#     print(number)
# continue
# Skips the current iteration and moves to the next one.

# Example:
# for number in range(1, 6):
#     if number == 3:
#         continue
#     print(number)

# 3. NESTED LOOPS — SYNTAX
# A loop inside another loop is called a nested loop.
# Example:
# for i in range(3):
#     for j in range(3):
#         print(i, j)

# 4. PRACTICE QUESTIONS

# Q1. PRINT NUMBERS
# Use a for loop to print numbers from 1 to 10.
for number in range(1,11):
    print(number)

# Q2. PRINT EVEN NUMBERS
# Use a for loop to print all even numbers from 1 to 20.
for number in range(1,21):
    if number % 2 == 0:
        print(number)

# Q3. PRINT ODD NUMBERS
# Use a for loop to print all odd numbers from 1 to 20.
for number in range(1,21):
    if number % 2 != 0:
        print(number)

# Q4. RANGE WITH STEP
# Use range() to print: 0, 5, 10, 15, 20, 25, 30
for num in range(0, 32):
    if num % 5 == 0:
        print( num)

# Q5. REVERSE RANGE
# Use range() to print numbers from 10 down to 1.
for num in range(11,0,-1):
    print(num)

# Q6. LOOP THROUGH A LIST
# Create: students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
# Use a for loop to print each student.
students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
for name in students:
    print(name)

# Q7. LOOP THROUGH COURSES
# Create a list: courses = ["Python", "SQL", "Excel", "Power BI"]
# Print each course using a for loop.
courses = ["Python", "SQL", "Excel", "Power BI"]
for name in courses:
    print(name)

# Q8. SUM OF NUMBERS
# Use a for loop to calculate the sum of numbers from 1 to 100.
# Store the result in `total`. Print the result.
total = 0
for num in range(1,101):
    total = num + total
    print(total)

# Q9. MULTIPLICATION TABLE
# Create: number = 7
# Use a for loop to print the multiplication table of 7 from 1 to 10.
number = 7
for x in range(1,11):
    multiplication_7 = number * x
    print(multiplication_7)

# Q10. COUNT ITEMS
# Create: students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
# Use a loop to count the number of students. Store the result in `student_count`. Print it.
students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
student_count = 0
for x in students:
    student_count += 1
print(student_count)

# Q11. FIND THE HIGHEST NUMBER
# Create: numbers = [25, 67, 12, 89, 45, 91, 34]
# Use a loop to find the highest number. Do not use max(). Store the result in `highest`.
# Print it.
numbers = [25, 67, 12, 89, 45, 91, 34]
highest = numbers[0]
for x in numbers:
    if x > highest:
        highest = x
print(highest)

# Q12. FIND THE LOWEST NUMBER
# Create: numbers = [25, 67, 12, 89, 45, 91, 34]
# Use a loop to find the lowest number. Do not use min().
# Store the result in `lowest`. Print it.
numbers = [25, 67, 12, 89, 45, 91, 34]
lowest = numbers[0]
for x in numbers:
    if x < lowest:
        lowest = x
print(lowest)

# Q13. COUNT STUDENTS ABOVE 70
# Create: marks = [45, 78, 92, 35, 88, 67, 95]
# Use a loop to count how many students scored above 70.
# Store the result in `count`. Print it.
marks = [45, 78, 92, 35, 88, 67, 95]
count = 0
for x in marks:
    if x > 70:
        count += 1
print(count)

# Q14. CALCULATE AVERAGE
# Create: marks = [75, 82, 91, 68, 88]
# Use a loop to calculate: total marks, average marks. Do not use sum().
marks = [75, 82, 91, 68, 88]
total = 0
for x in marks:
    total = total + x
print(f"Total marks is {total}")
average_marks = total/ len(marks)
print(f"Average marks is {average_marks}")

# Q15. PRINT ONLY PASSING MARKS
# Create: marks = [35, 78, 42, 91, 29, 65, 88]
# Use a loop to print only marks greater than or equal to 40.
marks = [35, 78, 42, 91, 29, 65, 88]
for num in marks:
    if num >= 40:
        print(num)

# Q16. PRINT ONLY FAILED MARKS
# Using: marks = [35, 78, 42, 91, 29, 65, 88]. Use a loop to print only marks below 40.
marks = [35, 78, 42, 91, 29, 65, 88]
for num in marks:
    if num < 40:
        print(num)

# Q17. WHILE LOOP
# Use a while loop to print numbers from 1 to 10.
num = 0
while num < 10:
    num = num + 1
    print(num)

# Q18. WHILE LOOP SUM
# Use a while loop to calculate the sum of numbers from 1 to 50.
# Store the result in `total`. Print the result.
num = 0
total = 0
while num < 50:
    num = num + 1
    total = num + total
print(total)

# Q19. BREAK
# Use a for loop from 1 to 20. Stop the loop when the number reaches 10.
# Use break.
for x in range(1,21):
    print(x)
    if x == 10:
        break

# Q20. CONTINUE
# Use a for loop from 1 to 20. Print all numbers except 10.
# Use continue.
for x in range(1,21):
    if x == 10:
     continue
    print(x)

# Q21. SEARCH FOR A STUDENT
# Create: students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]. Search for "Rahul" using a loop.
# If found, print: "Student found", Otherwise print: "Student not found"
# Use break when the student is found.
students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
for x in students:
    if x == "Rahul":
        print("Student found")
        break
else:
    print("Student not found")

# Q22. COUNT VOWELS
# Create: text = "Python Programming"
# Use a loop to count how many vowels (a, e, i, o, u) are present.
# Store the result in `vowel_count`. Print it.
text = "Python Programming"
vowel = ["a","e","i","o","u"]
vowel_count = 0
for x in text:
    if x in vowel:
        vowel_count = vowel_count + 1
        print(vowel_count)

# Q23. NESTED LOOP
# Use nested loops to print the following pattern:
# *
# **
# ***
# ****
# *****
# Use a for loop inside another for loop.
for i in range(1, 6):       # lines
    for j in range(1,6):      # stars
        print("*", end="")
    print()

# Q24. STUDENT ANALYSIS
# Create: students = ["Aman", "Riya", "Rahul", "Priya", "Neha"], marks = [75, 82, 35, 91, 68]
# Use loops to:
# 1. Print each student's name and marks.
# 2. Count how many students passed.
# 3. Count how many students failed.
# 4. Find the highest marks.
# Store important results in variables.
students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
marks = [75, 82, 35, 91, 68]
passed = 0
failed = 0
highest = marks[0]
for i in range(len(students)):
    print(students[i], marks[i])
    if marks[i] >= 40:
        passed = passed + 1
    if marks[i] < 40:
        failed = failed + 1
    if marks[i] > highest:
        highest = marks[i]
print("Passed:", passed)
print("Failed:", failed)
print("Highest marks:", highest)

# Q25. MINI CHALLENGE ⭐
# Create: students = ["Aman", "Riya", "Rahul", "Priya", "Neha"], marks = [85, 72, 91, 38, 67]
# Use loops to:
# 1. Print every student's name and marks.
# 2. Count passing students.
# 3. Count failing students.
# 4. Find the highest marks.
# 5. Find the lowest marks.
# 6. Calculate the total marks.
# 7. Calculate the average marks.
# 8. Print the names of students who scored 80 or above.
# Do not use max(), min(), or sum(). Solve the calculations using loops.
students = ["Aman", "Riya", "Rahul", "Priya", "Neha"]
marks = [85, 72, 91, 38, 67]
passed = 0
failed = 0
highest = marks[0]
lowest = marks[0]
total = 0
for i in range(len(students)):
    # 1. Print student's name and marks
    print(students[i], marks[i])
    # 2. Count passing students
    if marks[i] >= 40:
        passed = passed + 1
    # 3. Count failing students
    if marks[i] < 40:
        failed = failed + 1
    # 4. Find highest marks
    if marks[i] > highest:
        highest = marks[i]
    # 5. Find lowest marks
    if marks[i] < lowest:
        lowest = marks[i]
    # 6. Calculate total marks
    total = total + marks[i]
    # 8. Students who scored 80 or above
    if marks[i] >= 80:
        print("80 or above:", students[i])
# 7. Calculate average
average = total / len(marks)
print("Passed:", passed)
print("Failed:", failed)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Total marks:", total)
print("Average marks:", average)