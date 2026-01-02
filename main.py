# Student Marks Management System

student = {}

# Input student name
name = input("Enter student name: ")
student["Name"] = name
subjects = ["Java", "Python", "C++", "C#", "DBMS"]
total_marks = 0

# Input marks
for subject in subjects:
    marks = int(input(f"Enter marks for {subject}: "))
    student[subject] = marks
    total_marks += marks

# Calculate percentage
percentage = total_marks / len(subjects)

# Determine grade
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Fail"

# Store results
student["Total"] = total_marks
student["Percentage"] = percentage
student["Grade"] = grade

# Display result
print("\n--- Student Result ---")
for key, value in student.items():
    print(f"{key}: {value}")
