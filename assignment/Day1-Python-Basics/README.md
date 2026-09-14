# Day 1: Python Basics

This folder introduces Python through small business-style programs: bank accounts, customers, employee salary, electricity bills, and movie tickets.

## Learning Goals

- Store values with variables and choose useful data types.
- Read input and convert text to `int`, `float`, or `str`.
- Use arithmetic, comparisons, and conditional logic.
- Format readable output with f-strings.
- Break a problem into inputs, calculations, and output.

## Core Concepts

### Variables and Types

```python
customer_name = "Sonal"
age = 25
balance = 1250.50
is_active = True
```

Python assigns the type at runtime. Use `type(value)` while learning to inspect a value.

### Input and Conversion

`input()` always returns text, so convert it before doing calculations:

```python
price = float(input("Price: "))
quantity = int(input("Quantity: "))
total = price * quantity
```

### Conditions

```python
if total >= 1000:
    discount = 0.10
else:
    discount = 0
final_price = total - (total * discount)
```

### Strings and Output

```python
print(f"{customer_name} owes Rs. {final_price:.2f}")
```

The `.2f` formats a number to two decimal places.

## File Guide

| File | Practice |
| --- | --- |
| `bank_account.py` | Account data, balance calculations, and transactions |
| `customer.py` | Customer details and formatted output |
| `employee_salary.py` | Salary and compensation calculations |
| `electricity_bill.py` | Usage-based bill calculation |
| `movie_ticket.py` | Ticket pricing and conditional totals |
| `assign.ipynb` | Interactive notebook practice |

## A Problem-Solving Pattern

```text
1. Identify inputs.
2. Convert input to the correct type.
3. Calculate intermediate values.
4. Apply business rules with if/elif/else.
5. Print a clear result.
```

## Important Differences

- `int` stores whole numbers; `float` stores decimal values.
- `=` assigns a value; `==` compares two values.
- `and` requires both conditions; `or` requires at least one.
- `print()` displays a value; `return` sends a value back from a function.

## Exercises

1. Add a senior-citizen discount to the movie ticket program.
2. Reject negative bank deposits and invalid quantities.
3. Add slab-based electricity pricing.
4. Format every currency result to two decimal places.
5. Write a program that converts Celsius to Fahrenheit.

## Interview Check

**Why convert `input()` values?** `input()` returns a string. Arithmetic requires numeric types such as `int` or `float`.

**What is a variable?** A name that refers to a value in memory.

**What happens when an `if` condition is false?** Python checks the next `elif` or runs the `else` block when one exists.
