from tabulate import tabulate

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    name = input("Enter student name: ")
    python_marks = float(input("Enter Python marks: "))
    sql_marks = float(input("Enter SQL marks: "))
    powerbi_marks = float(input("Enter Power BI marks: "))
    attendance = float(input("Enter attendance %: "))
    print("-----------------------------------------------")

    if not (0 <= python_marks <= 100 and 0 <= sql_marks <= 100 and 0 <= powerbi_marks <= 100 and 0 <= attendance <= 100):
        print("Invalid data")
        continue

    total = python_marks + sql_marks + powerbi_marks
    average = total / 3

    passed = (python_marks >= 40 and sql_marks >= 40 and powerbi_marks >= 40 and attendance >= 75)

    if not passed:
        grade = "F"
    elif average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    scholarship = passed and average >= 85 and attendance >= 90

    students.append([
        name, python_marks, sql_marks, powerbi_marks, attendance, total, round(average, 2),
        "Pass" if passed else "Fail", grade,
        "Yes" if scholarship else "No"
    ])

passed_students = [s[0] for s in students if s[7] == "Pass"]
failed_students = [s[0] for s in students if s[7] == "Fail"]
scholarship_students = [s[0] for s in students if s[9] == "Yes"]

print("\nSTUDENT RESULT REPORT")

print(tabulate(
    students,
    headers=["Name","Python","SQL","Power BI","Attendance","Total","Average","Result","Grade","Scholarship"],
    tablefmt="grid"
))

print("\nPassed Students:", passed_students)
print("Failed Students:", failed_students)
print("Scholarship Students:", scholarship_students)