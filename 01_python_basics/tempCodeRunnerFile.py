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