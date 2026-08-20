# ============================================================
# PYTHON BASICS — SETS
# ============================================================


# 1. SETS — SYNTAX
# A set is an unordered collection of unique items. Sets are created using curly brackets {}.
# Example: departments = {"IT", "HR", "Finance", "Marketing"}
# A set automatically removes duplicate values.
# Example: numbers = {10, 20, 20, 30, 30, 40}

# 2. NOTES
# Sets are: Unordered, Changeable, Do not allow duplicate values, Do not support indexing like lists and tuples
# Example: departments = {"IT", "HR", "Finance"}
# You cannot access a set item using an index: departments[0]
# This will cause an error.
# Sets are useful when you want to store unique values.
# Example: departments = {"IT", "HR", "IT", "Finance"}-> Duplicate "IT" will be removed.

# 3. SET METHODS — SYNTAX

# add(): Adds one item to a set.
# set.add(item)
# update(): Adds multiple items to a set.
# set.update(other_collection)
# remove(): Removes a specific item.
# set.remove(item)
# discard(): Removes an item if it exists.
# set.discard(item)
# pop(): Removes an item from the set.
# set.pop()
# clear(): Removes all items.
# set.clear()

# 4. SET OPERATIONS — SYNTAX

# union(): Combines items from two sets.
# set1.union(set2)
# intersection(): Returns items that exist in both sets.
# set1.intersection(set2)
# difference(): Returns items present in the first set but not the second.
# set1.difference(set2)
# symmetric_difference(): Returns items that are in either set but not in both.
# set1.symmetric_difference(set2)


# 5. PRACTICE QUESTIONS

# Q1. CREATE A SET
# Create a set called `departments` containing: "IT", "HR", "Finance", "Marketing"
# Print the set.
departments = { "IT", "HR", "Finance", "Marketing" }
print(departments)
print(type(departments))

# Q2. REMOVE DUPLICATES
# Create: numbers = {10, 20, 20, 30, 30, 40, 40}. Print the set.
# Observe what happens to the duplicate values.
numbers = {10, 20, 20, 30, 30, 40, 40}
print(numbers)
# dublicate is not there.

# Q3. ADD AN ITEM
# Create: skills = {"Python", "SQL", "Excel"}. Add "Power BI" to the set using add().
# Print the updated set.
skills = {"Python", "SQL", "Excel"}
update_skills = skills.add("Power BI")
print(skills)

# Q4. UPDATE A SET
# Create: skills = {"Python", "SQL"}, new_skills = {"Power BI", "Excel", "Statistics"}
# Add all items from new_skills to skills using update().
# Print the updated set.
skills = {"Python", "SQL"}
new_skills = {"Power BI", "Excel", "Statistics"}
skills.update(new_skills)
print(skills)

# Q5. REMOVE AN ITEM
# Create: courses = {"Python", "SQL", "Excel", "Power BI"}
# Remove "Excel" using remove(). Print the updated set.
courses = {"Python", "SQL", "Excel", "Power BI"}
updated_set = courses.remove("Excel")
print(courses)

# Q6. DISCARD AN ITEM
# Create: departments = {"IT", "HR", "Finance"}. Use discard() to remove "Marketing".
# Observe what happens when the item does not exist. Print the set.
departments = {"IT", "HR", "Finance"}
departments.discard("Marketing")
print(departments)

# Q7. UNION
# Create: python_students = {"Aman", "Riya", "Rahul", "Priya"}, sql_students = {"Rahul", "Priya", "Neha", "Arjun"}
# Use union() to find all students who are studying Python or SQL.
# Store the result in `all_students`. Print it.
python_students = {"Aman", "Riya", "Rahul", "Priya"}
sql_students = {"Rahul", "Priya", "Neha", "Arjun"}
all_students = python_students.union(sql_students)
print(all_students)

# Q8. INTERSECTION
# Using: python_students = {"Aman", "Riya", "Rahul", "Priya"}, sql_students = {"Rahul", "Priya", "Neha", "Arjun"}
# Find the students who are studying both Python and SQL. Store the result in `both_courses`.
# Print it.
python_students = {"Aman", "Riya", "Rahul", "Priya"}
sql_students = {"Rahul", "Priya", "Neha", "Arjun"}
both_courses = python_students.intersection(sql_students)
print(both_courses)

# Q9. DIFFERENCE
# Using: python_students = {"Aman", "Riya", "Rahul", "Priya"}, sql_students = {"Rahul", "Priya", "Neha", "Arjun"}
# Find the students who are studying Python but NOT SQL. Store the result in `python_only`.
# Print it.
python_students = {"Aman", "Riya", "Rahul", "Priya"}
sql_students = {"Rahul", "Priya", "Neha", "Arjun"}
python_only = python_students.difference(sql_students)
print(python_only)

# Q10. MINI CHALLENGE ⭐
# You have two sets of students:data_analytics_students = {"Aman", "Riya", "Rahul", "Priya", "Neha"} ,python_students = {"Rahul", "Priya", "Neha", "Arjun", "Kiran"}
# Find:
# 1. All unique students from both courses.
# 2. Students studying both courses.
# 3. Students studying Data Analytics but not Python.
# 4. Students studying Python but not Data Analytics.
# Store each result in a separate variable. Print all results clearly.
data_analytics_students = {"Aman", "Riya", "Rahul", "Priya", "Neha"}
python_students = {"Rahul", "Priya", "Neha", "Arjun", "Kiran"}
unique_students = data_analytics_students.union(python_students)
print("Unique students:", unique_students)
both_courses = data_analytics_students.intersection(python_students)
print("Students studying both:", both_courses)
data_analytics_only = data_analytics_students.difference(python_students)
print("Data Analytics only:", data_analytics_only)
python_only = python_students.difference(data_analytics_students)
print("Python only:", python_only)