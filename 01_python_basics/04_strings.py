# ============================================================
# PYTHON BASICS — STRINGS
# ============================================================

# 1. STRINGS — SYNTAX - A string is a sequence of characters enclosed inside single quotes or double quotes.
# Examples:name = "John Doe", city = 'New York'

# Multi-line string: message = """This is a multi-line string."""
# Access a character using an index:
# text[index]
# Example: text = "Python"
# print(text[0])

# Negative indexing: text[-1]
# Example: print(text[-1])

# String slicing: text[start:end]
# Example: print(text[0:3])

# 2. NOTES - Strings are used to store text.
# Strings can be written using: "double quotes",'single quotes'
# Python uses zero-based indexing. The first character has index 0.
# Example: Python -  P = 0, y = 1, t = 2, h = 3, o = 4, n = 5       

# Negative indexing starts from the end. -1 refers to the last character. Strings can be sliced to extract part of a string.
# Example: text = "Python", text[0:3] gives "Pyt"
# Strings are immutable. This means individual characters cannot be changed directly.
# Example: text = "Python", text[0] = "J"   # This will cause an error.

# 3. STRING METHODS — SYNTAX- Common string methods:
# upper()- Converts text to uppercase.
# text.upper()
# lower()- Converts text to lowercase.
# text.lower()
# capitalize()- Capitalizes the first character.
# text.capitalize()
# title()- Capitalizes the first character of each word.
# text.title()
# strip()- Removes spaces from the beginning and end.
# text.strip()
# replace()- Replaces part of a string.
# text.replace("old", "new")
# split()- Splits a string into a list.
# text.split()
# find()- Finds the position of text.
# text.find("Python")
# count()- Counts occurrences of text.
# text.count("a")
# startswith()- Checks whether a string starts with specific text.
# text.startswith("Py")
# endswith()- Checks whether a string ends with specific text.
# text.endswith("on")

# 4. F-STRINGS — SYNTAX- F-strings allow variables to be inserted directly inside a string.
# Example: name = "Muskan",age = 26
# print(f"My name is {name} and I am {age} years old.")


# 5. PRACTICE QUESTIONS

# Q1. CREATE A STRING
# Create a variable called `course` and store: "Python Programming".
# Print the variable.
course = "Python Programming"
print(course)

# Q2. STRING LENGTH
# Create:text = "Data Analytics". Use len() to find the number of characters.
# Store the result in `length`.Print the result.
text = "Data Analytics"  # space also take lenght.
lenght = len(text)
print(lenght)

# Q3. ACCESS CHARACTERS
# Create: word = "Python"
# Print: the first character, the third character, the last character.
word = "Python"
print(word[1],word[3],word[-1])

# Q4. NEGATIVE INDEXING
# Create: word = "Analytics". Use negative indexing to print: the last character, the second-last character
word = "Analytics"
print(word[-1],word[-2])

# Q5. STRING SLICING
# Create: text = "Python Programming".  Use slicing to print: "Python", "Programming", "Python Programming".
text = "Python Programming"
print(text[0:6])
print(text[7:18])
print(text[0:18])

# Q6. REVERSE A STRING
# Create: text = "Python".Use string slicing to reverse the string.
# Print the reversed string.
text = "Python"
reverse = text[::-1]
print(reverse)

# Q7. UPPERCASE AND LOWERCASE
# Create: text = "Data Analytics". Print: the text in uppercase, the text in lowercase.
text = "Data Analytics"
upp = text.upper()
low = text.lower()
print(upp, low)

# Q8. CAPITALIZE AND TITLE
# Create: text = "python programming language". Use: capitalize(), title().
# Print both results.
text = "python programming language"
cap = text.capitalize()
tit = text.title()
print(cap, tit)

# Q9. REMOVE SPACES
# Create: text = "   Python Programming   ". Use strip() to remove spaces from the beginning and end.
# Store the result in `clean_text`. Print it.
text = "   Python Programming   "
clean_text = text.strip()
print(clean_text)

# Q10. REPLACE TEXT".
# Create: text = "I am learning Java". Replace "Java" with "Python".
# Store the result in `new_text`. Print it.
text = "I am learning Java"
new_text = text.replace("Java", "Python")
print(new_text)

# Q11. FIND TEXT
# Create: text = "I am learning Python". Use find() to find the position of "Python".
# Store the result in `position`. Print it.
text = "I am learning Python"
position = text.find("Python")
print(position)    #index of p is 14

# Q12. COUNT CHARACTERS
# Create:text = "banana". Use count() to find how many times "a" appears.
# Store the result in `count_a`. Print it.
text = "banana"
count_a = text.count("a")       
print(count_a)

# Q13. STARTS WITH AND ENDS WITH
# Create: email = "student@example.com". Check whether the email: starts with "student", ends with ".com"
# Print both results.
email = "student@example.com"
str = email.startswith("student")
print(str)
en = email.endswith(".com")
print(en)

# Q14. SPLIT A STRING
# Create: students = "Aman,Riya,Rahul,Priya". Use split() to convert the string into a list of names.
# Store it in `student_list`. Print the list.
students = "Aman,Riya,Rahul,Priya"
student_list = students.split()
print(student_list)

# Q15. JOIN STRINGS
# Create: first_name = "Rahul", last_name = "Kumar". Combine them into: "Rahul Kumar"
# Store the result in `full_name`. Print it.
first_name = "Rahul"
last_name = "Kumar" 
full_name = first_name + " " + last_name
print(full_name)

# Q16. F-STRING
# Create: name = "Muskan", age = 26, city = "Delhi".
# Use an f-string to print: "My name is Muskan, I am 26 years old and I live in Delhi."
name = "Muskan" 
age = 26
city = "Delhi"
print(f"My name is {name} and my age is {age}. I live in {city}.")

# Q17. STRING CLEANING
# Create: text = "   STUDENT ANALYTICS   ". Remove the extra spaces and convert the text to lowercase.
# Store the result in `clean_text`. Print it.
text = "   STUDENT ANALYTICS   "
clean_text = text.strip().lower()
print(clean_text)

# Q18. STRING ANALYSIS
# Create: text = "Python is easy and Python is powerful".
# Find:
# - length of the string
# - number of times "Python" appears
# - position of the first "Python"
# Print all three results.
text = "Python is easy and Python is powerful"
leng = len(text)
print(leng)
f = text.find("Python")
print(f)
c = text.count("Python")
print(c)

# Q19. STUDENT EMAIL
# Create:email = "muskan.student@gmail.com".  Perform the following:
# 1. Check whether the email ends with ".com".
# 2. Check whether it contains "@gmail".
# 3. Extract the username before "@".
# Print all three results.
email = "muskan.student@gmail.com"

print(email.endswith(".com"))
print("@gmail" in email)
print(email[:email.index("@")])

# Q20. MINI CHALLENGE ⭐
# Create: student_name = "  Rahul Kumar  ", course = "python programming", marks = 85.
# Perform the following:
# 1. Remove extra spaces from student_name.
# 2. Convert student_name to title case.
# 3. Convert course to title case.
# 4. Create a sentence using an f-string: "Rahul Kumar is studying Python Programming and scored 85 marks."
# Print the final sentence. Also print: student name length, course length.
student_name = "  Rahul Kumar  "
course = "python programming"
marks = 85
s = student_name.strip()
d = student_name.title()
f = course.title()
h = len(student_name)
i = len(course)
print(s)
print(d)
print(f)
print(h)
print(i)
print(f"{s} is studying {f} and have scored {marks} marks.")
