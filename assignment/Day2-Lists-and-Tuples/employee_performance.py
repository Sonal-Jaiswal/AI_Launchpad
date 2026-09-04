# from tabulate import tabulate

# total_employee = int(input("Enter number of employees: "))


# table_data = []

# for emp in employees:
#     table_data.append([
#         emp["name"],
#         emp["salary"],
#         emp["score"],
#         emp["category"],
#         emp["bonus"],
#         emp["final_salary"]
#     ])

# headers = ["Name", "Salary", "Score", "Category", "Bonus", "Final Salary"]


# employees = []
# total_bonus = 0

# for i in range(total_employee):
#     print(f"\nEmployee {i + 1}")

#     employee_name = input("Enter name: ")
#     monthly_salary = float(input("Enter monthly salary: "))
#     performance_score = int(input("Enter performance score: "))

#     if monthly_salary <= 0:
#         print("Salary should be greater than zero")
#         continue

#     if performance_score < 0 or performance_score > 100:
#         print("Performance score should be between 0 and 100")
#         continue

    
#     if performance_score >= 90:
#         category = "Outstanding"
#         bonus_percent = 20
#     elif performance_score >= 75:
#         category = "Very Good"
#         bonus_percent = 10
#     elif performance_score >= 60:
#         category = "Good"
#         bonus_percent = 5
#     elif performance_score >= 40:
#         category = "Needs Improvement"
#         bonus_percent = 0
#     else:
#         category = "Unsatisfactory"
#         bonus_percent = 0

#     bonus_amount = monthly_salary * bonus_percent / 100
#     final_salary = monthly_salary + bonus_amount

#     total_bonus += bonus_amount

#     emp = {
#         "name": employee_name,
#         "salary": monthly_salary,
#         "score": performance_score,
#         "category": category,
#         "bonus": bonus_amount,
#         "final_salary": final_salary
#     }

#     employees.append(emp)


# eligible_employees = [emp for emp in employees if emp["score"] >= 75]

# # print("\n--- All Employee Records ---")
# # for emp in employees:
# #     print(emp)

# print("\n--- Bonus Eligible Employees (Score >= 75) ---")
# for emp in eligible_employees:
#     print(emp["name"])

# print("\nTotal Bonus Paid by Organization:", total_bonus)


# print(tabulate(table_data, headers=headers, tablefmt="grid"))


from tabulate import tabulate

total_employee = int(input("Enter number of employees: "))

employees = []
total_bonus = 0

for i in range(total_employee):
    print(f"\nEmployee {i + 1}")

    employee_name = input("Enter name: ")
    monthly_salary = float(input("Enter monthly salary: "))
    performance_score = int(input("Enter performance score: "))

    if monthly_salary <= 0:
        print("Salary should be greater than zero")
        continue

    if performance_score < 0 or performance_score > 100:
        print("Performance score should be between 0 and 100")
        continue

    if performance_score >= 90:
        category = "Outstanding"
        bonus_percent = 20
    elif performance_score >= 75:
        category = "Very Good"
        bonus_percent = 10
    elif performance_score >= 60:
        category = "Good"
        bonus_percent = 5
    elif performance_score >= 40:
        category = "Needs Improvement"
        bonus_percent = 0
    else:
        category = "Unsatisfactory"
        bonus_percent = 0

    bonus_amount = monthly_salary * bonus_percent / 100
    final_salary = monthly_salary + bonus_amount

    total_bonus += bonus_amount

    employees.append({
        "name": employee_name,
        "salary": monthly_salary,
        "score": performance_score,
        "category": category,
        "bonus": bonus_amount,
        "final_salary": final_salary
    })

# Create table data after employees are populated
table_data = []

for emp in employees:
    table_data.append([
        emp["name"],
        emp["salary"],
        emp["score"],
        emp["category"],
        emp["bonus"],
        emp["final_salary"]
    ])

headers = ["Name", "Salary", "Score", "Category", "Bonus", "Final Salary"]

print("\n--- All Employee Records ---")
print(tabulate(table_data, headers=headers, tablefmt="grid"))

print("\nTotal Bonus Paid:", total_bonus)