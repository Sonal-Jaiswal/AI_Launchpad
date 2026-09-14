# Day 2: Lists and Tuples

This folder practices collections through employee records, shopping bills, student results, inventory, expenses, Aadhaar-style records, and ration-card data.

## Learning Goals

- Store multiple values in lists and tuples.
- Index, slice, update, sort, and iterate over collections.
- Choose mutable lists or immutable tuples appropriately.
- Combine collections with dictionaries and conditions.
- Calculate totals, averages, grades, stock, and expenses.

## Lists

A list is ordered and mutable:

```python
items = ["rice", "milk", "eggs"]
items.append("bread")
items[0] = "brown rice"
print(items[1:3])
```

Useful methods include `append`, `extend`, `insert`, `remove`, `pop`, `sort`, and `reverse`.

## Tuples

A tuple is ordered but immutable:

```python
coordinates = (19.07, 72.87)
latitude, longitude = coordinates
```

Use tuples for fixed records or values that should not be changed accidentally.

## Iteration and Comprehensions

```python
prices = [100, 250, 75]
totals = [price * 1.18 for price in prices]
```

A loop is often clearer for beginners or when several statements are needed.

## File Guide

| File | Practice |
| --- | --- |
| `list.py` | List operations and collection basics |
| `employee_performance.py` | Employee data and performance decisions |
| `shopping_bill.py` | Items, quantities, and bill totals |
| `student_result.py` | Marks, grades, and results |
| `inventory_stock.py` | Product stock and availability |
| `expense_tracker.py` | Expense totals and categories |
| `aadhaar.py` | Record-style data handling |
| `ration_card.py` | Eligibility and household records |
| `assignments.py`, `test.py` | Additional practice |

## Important Differences

- List: mutable, written with `[]`.
- Tuple: immutable, written with `()`.
- `append(x)` adds one item; `extend(values)` adds several items.
- `remove(x)` removes by value; `pop(index)` removes by position and returns the item.
- `sort()` changes a list; `sorted(values)` returns a new sorted list.

## Common Pitfall

Assignment creates an alias:

```python
first = [1, 2]
second = first
second.append(3)
# first is now [1, 2, 3]
```

Use `second = first.copy()` when an independent list is needed.

## Exercises

1. Find the highest and lowest expense.
2. Calculate a student's average and assign a grade.
3. Add low-stock warnings to the inventory program.
4. Remove duplicate items while preserving order.
5. Create a tuple-based product record and unpack it.

## Interview Check

**Why are tuples useful?** They communicate that a collection should not change and can be used where hashable fixed values are needed.

**What is slicing?** Selecting a range with `values[start:stop:step]`; the stop index is excluded.
