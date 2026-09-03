# Assignment 2: Employee Salary and Bonus Calculator
 
# Create a Python program to calculate an employee’s final monthly salary.
 
# Requirements- 
# Accept employee name, basic salary, performance rating, and years of service.
# Performance rating must be between 1 and 5.
# Calculate the bonus:
# Rating 5 and service of 5 years or more: 20% bonus
# Rating 5 and service below 5 years: 15% bonus
# Rating 4: 10% bonus
# Rating 3: 5% bonus
# Rating below 3: No bonus
# Deduct 5% tax if the final salary exceeds ₹50,000.
# Display basic salary, bonus, tax, and net salary.
# Display an error message for invalid salary, rating, or service years.

emp_name = input("Enter Employee Name: ")
salary = float(input("Enter Basic Salary: "))
rating = int(input("Enter Performance Rating (1-5): "))
service_years = int(input("Enter Years of Service: "))

if salary <= 0:
    print("Error: Invalid Salary")

elif rating < 1 or rating > 5:
    print("Error: Performance Rating must be between 1 and 5")

elif service_years < 0:
    print("Error: Invalid Years of Service")

else:
    if rating == 5:
        if service_years >= 5:
            bonus = salary * 0.20
        else:
            bonus = salary * 0.15
    elif rating == 4:
        bonus = salary * 0.10
    elif rating == 3:
        bonus = salary * 0.05
    else:
        bonus = 0
    final_salary = salary + bonus
    if final_salary > 50000:
        tax = final_salary * 0.05
    else:
        tax = 0
    net_salary = final_salary - tax
    print("\n------ Salary Details ------")
    print("Employee Name :", emp_name)
    print("Basic Salary  : ₹", salary)
    print("Bonus         : ₹", bonus)
    print("Tax Deduction : ₹", tax)
    print("Net Salary    : ₹", net_salary)