grade = input("Enter letter grade: ").upper()

grades = {
    "A" : 4.0,
    "B" : 3.0,
    "C" : 2.0,
    "D" : 1.0,
    "F" : 0.0
}

while grade not in grades:
    grade = input("Enter letter grade: ").upper()

print(f"GPA: {grades[grade]}")

