# ============================================================
# PYTHON BASICS — EXCEPTIONS
# ============================================================

# 1. EXCEPTIONS — SYNTAX- An exception is an error that occurs while a program is running.
# Example: number = 10
# result = number / 0 # This produces a ZeroDivisionError.

# Basic try-except syntax:
# try:
#     statement_that_might_cause_error
# except:
#     statement_to_handle_error

# Example:
# try:
#     number = 10 / 0
# except:
#     print("An error occurred")


# 2. NOTES

# Exception handling allows a program to handle errors without immediately stopping the entire program.
# The code that might cause an error is placed inside the try block.
# The code that handles the error is placed inside the except block.
# It is better to catch a specific exception when possible.
# Example:
# try:
#     number = int("abc")
# except ValueError:
#     print("Invalid number")


# Common exceptions: ValueError- Occurs when a value has the correct type but an invalid value.
# Example: int("abc")

# TypeError: Occurs when an operation is performed on an inappropriate data type.
# Example: "10" + 5

# ZeroDivisionError- Occurs when a number is divided by zero.
# Example: 10 / 0

# IndexError: Occurs when trying to access an index that does not exist.
# Example: numbers = [10, 20], numbers[5]

# KeyError- Occurs when trying to access a dictionary key that does not exist.
# Example: student = {"name": "Rahul"}
# student["age"]

# 3. TRY-EXCEPT-ELSE-FINALLY — SYNTAX
# try:
#     code_that_might_fail
# except SomeError:
#     code_to_handle_error
# else:
#     code_that_runs_if_no_error_occurs
# finally:
#     code_that_runs_whether_error_occurs_or_not

# Example:
# try:
#     number = int("100")
# except ValueError:
#     print("Invalid value")
# else:
#     print("Conversion successful")
# finally:
#     print("Program finished")

# 4. PRACTICE QUESTIONS


# Q1. BASIC TRY-EXCEPT
# Create: number = 10. Try to divide the number by zero.Use try-except to handle the error.
# Print: "Cannot divide by zero"
number = 10
try:
    result = number /0
except ZeroDivisionError:
    print("Cannot divide by zero")    

# Q2. VALUE ERROR
# Ask the user to enter a number using input(). Convert the input into an integer.
# Use try-except to handle ValueError if the user enters something that is not a valid number.
# Print an appropriate error message.
try:
    x = int(input("Enter the number: "))
    print("You entered:", x)
except ValueError:
    print("Please enter a valid number.") 

# Q3. TYPE ERROR
#  Create: number = 10, text = "5"
# Try to add them together. Handle the TypeError using try-except. Print an appropriate message.
number = 10
text = "5"
try:
    result = number + text
    print(result)
except TypeError:
    print("Invalid output")    

# Q4. ZERO DIVISION ERROR
# Ask the user to enter two numbers. Divide the first number by the second number.
# Handle: ValueError, ZeroDivisionError
# Print an appropriate message for each error.
# Your Answer:

# Q5. INDEX ERROR
# Create: numbers = [10, 20, 30]. Ask the user to enter an index. Try to print the item at that index.
# Handle: ValueError, IndexError. Print an appropriate message for each error.
# Q5. INDEX ERROR
numbers = [10, 20, 30]
try:
    i = int(input("Enter an index: "))
    print(numbers[i])
except ValueError:
    print("Please enter a valid integer.")
except IndexError:
    print("Index is out of range.")

# Q6. KEY ERROR
# Create: student = {
#     "name": "Rahul",
#     "age": 21,
#     "marks": 85 }
# Try to access a key called "city". Handle the KeyError. Print: "City information is not available."
student = { "name": "Rahul", "age": 21, "marks": 85 }
try:
    print(student["city"])
except KeyError:
    print("City information is not available.")

# Q7. MULTIPLE EXCEPTIONS
# Ask the user to enter two numbers. Perform division.
# Handle: ValueError, ZeroDivisionError. Use separate except blocks for each exception.
try:
    i = int(input("Enter 1st no."))
    i2 = i = int(input("Enter 2nd no."))
    result = i/ i2
    print(f"Division is {result}")
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError')   

# Q8. TRY-EXCEPT-ELSE
# Ask the user to enter a number. Try to convert it into an integer.
# If conversion is successful: print "Valid number"
# If conversion fails: print "Invalid number". Use try, except, and else.
try:
    i = int(input('Enter any number'))
    print('Number is valid')
except:
    print('Invalid number')

# Q9. TRY-EXCEPT-FINALLY
# Ask the user to enter a number. Try to convert it into an integer. Handle ValueError if the input is invalid.
# Use finally to print:"Program execution completed."
try:
    i = int(input('Enter any number'))
    print('Number is valid')
except ValueError:
    print('Invalid number')
print('Program execution completed.')

# Q10. MINI CHALLENGE ⭐
# Create a simple student marks program. Ask the user to enter: student name,  math marks, science marks, english marks
# Your program should:
# 1. Convert the marks into numbers.
# 2. Calculate total marks.
# 3. Calculate average marks.
# 4. Print the student's result.
# Handle invalid mark inputs using ValueError.
# Also make sure the program does not crash if invalid data is entered.
# Use: try, except, else, finally
# Print a suitable message when the program finishes.
# Q10. MINI CHALLENGE ⭐
try:
    name = input("Enter the name: ")
    maths = int(input("Enter your maths marks: "))
    science = int(input("Enter your science marks: "))
    english = int(input("Enter your English marks: "))
    total = maths + science + english
    avg = total / 3
except ValueError:
    print("Invalid marks! Please enter numbers only.")
else:
    print(f"\nStudent Name: {name}")
    print(f"Maths: {maths}")
    print(f"Science: {science}")
    print(f"English: {english}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {avg:.2f}")
finally:
    print("Student result program finished.")