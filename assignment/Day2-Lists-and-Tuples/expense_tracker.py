from tabulate import tabulate

budget = float(input("Enter monthly budget: "))
n = int(input("Enter number of expenses: "))

expenses = []
total_expenses = 0

for i in range(n):
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    print("-----------------------------------------------")

    if budget <= 0 or amount <= 0:
        print("Invalid data")
        continue

    expenses.append([description, category, amount])

    total_expenses += amount

remaining_budget = budget - total_expenses
used_percentage = (total_expenses / budget) * 100

if used_percentage > 100:
    status = "Budget Exceeded"
elif used_percentage >= 90:
    status = "Critical"
elif used_percentage >= 75:
    status = "Warning"
else:
    status = "Within Budget"

above_2000 = [e[0] for e in expenses if e[2] > 2000]

travel_expenses = [e[0] for e in expenses
if e[1].lower() == "travel"]

reduced_expenses = [round(e[2] * 0.9, 2) for e in expenses]

category_totals = {}

for e in expenses:
    category = e[1]
    amount = e[2]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

print("\nMONTHLY EXPENSE REPORT")

print(tabulate(
    expenses,
    headers=["Description","Category","Amount"],
    tablefmt="grid"
))

print("\nBudget:", budget)
print("Total Expenses:", total_expenses)
print("Remaining Budget:", remaining_budget)
print("Budget Used %:", round(used_percentage, 2))
print("Status:", status)

print("\nExpenses Above 2000:", above_2000)
print("Travel Expenses:", travel_expenses)
print("Expense Amounts After 10% Reduction:", reduced_expenses)

category_table = [[k, v] for k, v in category_totals.items()]

print("\nCATEGORY WISE TOTALS")

print(tabulate(
    category_table,
    headers=["Category", "Total"],
    tablefmt="grid"
))
